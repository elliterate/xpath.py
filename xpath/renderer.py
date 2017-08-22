from __future__ import unicode_literals

from cssselect import HTMLTranslator, parse
from functools import partial
from xpath.compat import bytes_, str_
from xpath.expression import ExpressionKind, ExpressionType
from xpath.literal import Literal
from xpath.utils import decode_bytes


class Renderer(object):
    """A rendering context for converting an XPath `Expression` into a valid string query."""

    _RENDER_METHOD_NAMES = {
        ExpressionKind.ANYWHERE: "_anywhere",
        ExpressionKind.ATTR: "_attribute",
        ExpressionKind.AXIS: "_axis",
        ExpressionKind.BINARY_OPERATOR: "_binary_operator",
        ExpressionKind.CHILD: "_child",
        ExpressionKind.CSS: "_css",
        ExpressionKind.DESCENDANT: "_descendant",
        ExpressionKind.FUNCTION: "_function",
        ExpressionKind.IS: "_is",
        ExpressionKind.TEXT: "_text",
        ExpressionKind.THIS_NODE: "_this_node",
        ExpressionKind.UNION: "_union",
        ExpressionKind.WHERE: "_where",
    }

    def __init__(self, exact=False):
        """
        Args:
            exact (bool, optional): Whether the generated queries should perform exact or
                approximate locator matches. Defaults to False.
        """

        self.exact = exact

    def render(self, node):
        """
        Converts a given XPath `Expression` into a corresponding string query.

        Args:
            node (Expression): An XPath `Expression` to convert.

        Returns:
            str: A valid XPath query corresponding to the given `Expression`.
        """

        args = [self._convert_argument(arg) for arg in node.arguments]
        render_method_name = self._RENDER_METHOD_NAMES[node.kind]
        render_method = getattr(self, render_method_name)
        return render_method(*args)

    def _convert_argument(self, argument):
        if isinstance(argument, ExpressionType):
            return self.render(argument)
        if isinstance(argument, list):
            return [self._convert_argument(element) for element in argument]
        if isinstance(argument, int):
            return str(argument)
        if isinstance(argument, (bytes_, str_)):
            return self._string_literal(argument)
        if isinstance(argument, Literal):
            return argument.value

    def _anywhere(self, element_names):
        return self._with_element_conditions("//", element_names)

    def _attribute(self, node, attribute_name):
        return "{0}/@{1}".format(node, attribute_name)

    def _axis(self, current, name, element_names):
        return self._with_element_conditions("{0}/{1}::".format(current, name), element_names)

    def _binary_operator(self, name, left, right):
        return "({0} {1} {2})".format(left, name, right)

    def _child(self, parent, element_names):
        return self._with_element_conditions("{0}/".format(parent), element_names)

    def _css(self, current, css_selector):
        # The given CSS selector may be a group selector (multiple selectors
        # delimited by commas), so we must parse out and convert the individual
        # selectors, then return their union.
        selectors = parse(css_selector)
        xpath_selectors = ["{0}//{1}".format(current, _selector_to_xpath(selector))
                           for selector in selectors]
        return self._union(*xpath_selectors)

    def _descendant(self, parent, element_names):
        return self._with_element_conditions("{0}//".format(parent), element_names)

    def _function(self, name, *arguments):
        return "{0}({1})".format(name, ", ".join(arguments))

    def _is(self, expr1, expr2):
        if self.exact:
            return self._binary_operator("=", expr1, expr2)
        else:
            return self._function("contains", expr1, expr2)

    def _string_literal(self, string):
        string = decode_bytes(string)

        def wrap(s):
            return "'{0}'".format(s)

        if "'" in string:
            parts = string.split("'")
            parts = map(wrap, parts)

            return "concat(" + ",\"'\",".join(parts) + ")"
        else:
            return wrap(string)

    def _text(self, current):
        return "{0}/text()".format(current)

    def _this_node(self):
        return "."

    def _union(self, *exprs):
        return " | ".join(exprs)

    def _where(self, expr, *predicate_exprs):
        predicates = ["[{0}]".format(predicate_expr) for predicate_expr in predicate_exprs]
        return "{0}{1}".format(expr, "".join(predicates))

    def _with_element_conditions(self, expression, element_names):
        if len(element_names) == 1:
            return "{0}{1}".format(expression, element_names[0])
        elif len(element_names) > 1:
            element_names_xpath = " | ".join(["self::{0}".format(e) for e in element_names])
            return "{0}*[{1}]".format(expression, element_names_xpath)
        else:
            return "{0}*".format(expression)


def to_xpath(node, exact=False):
    """
    Converts a given XPath `Expression` into a corresponding string query.

    Args:
        node (Expression): An XPath `Expression` to convert.
        exact (bool, optional): Whether the generated query should perform exact or approximate
            locator matches. Defaults to False.

    Returns:
        str: A valid XPath query corresponding to the given `Expression`.
    """

    return Renderer(exact=exact).render(node)


_selector_to_xpath = partial(HTMLTranslator().selector_to_xpath, prefix=None)
