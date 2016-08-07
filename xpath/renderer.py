from cssselect import HTMLTranslator, parse
from functools import partial
import sys
from xpath.expression import Expression, ExpressionKind, Union
from xpath.literal import Literal


class Renderer(object):
    """A rendering context for converting an XPath `Expression` into a valid string query."""

    _RENDER_METHOD_NAMES = {
        ExpressionKind.AND: "_and",
        ExpressionKind.ANYWHERE: "_anywhere",
        ExpressionKind.ATTR: "_attribute",
        ExpressionKind.AXIS: "_axis",
        ExpressionKind.CHILD: "_child",
        ExpressionKind.CONTAINS: "_contains",
        ExpressionKind.CSS: "_css",
        ExpressionKind.DESCENDANT: "_descendant",
        ExpressionKind.EQUALITY: "_equality",
        ExpressionKind.INVERSE: "_inverse",
        ExpressionKind.IS: "_is",
        ExpressionKind.NEXT_SIBLING: "_next_sibling",
        ExpressionKind.NODE_NAME: "_node_name",
        ExpressionKind.NORMALIZED_SPACE: "_normalized_space",
        ExpressionKind.ONE_OF: "_one_of",
        ExpressionKind.OR: "_or",
        ExpressionKind.PREVIOUS_SIBLING: "_previous_sibling",
        ExpressionKind.STARTS_WITH: "_starts_with",
        ExpressionKind.STRING: "_string_function",
        ExpressionKind.STRING_LENGTH_FUNCTION: "_string_length_function",
        ExpressionKind.SUBSTRING_FUNCTION: "_substring_function",
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
        if isinstance(argument, (Expression, Union)):
            return self.render(argument)
        if isinstance(argument, list):
            return [self._convert_argument(element) for element in argument]
        if isinstance(argument, int):
            return str(argument)
        if _is_string(argument):
            return self._string_literal(argument)
        if isinstance(argument, Literal):
            return argument.value

    def _and(self, expr1, expr2):
        return "({0} and {1})".format(expr1, expr2)

    def _anywhere(self, node):
        return "//{0}".format(node)

    def _attribute(self, node, attribute_name):
        return "{0}/@{1}".format(node, attribute_name)

    def _axis(self, parent, axis, element_name):
        return "{0}/{1}::{2}".format(parent, axis, element_name)

    def _child(self, parent, element_name):
        return "{0}/{1}".format(parent, element_name)

    def _contains(self, expr, value):
        return "contains({0}, {1})".format(expr, value)

    def _css(self, current, css_selector):
        # The given CSS selector may be a group selector (multiple selectors
        # delimited by commas), so we must parse out and convert the individual
        # selectors, then return their union.
        selectors = parse(css_selector)
        xpath_selectors = ["{0}//{1}".format(current, _selector_to_xpath(selector))
                           for selector in selectors]
        return self._union(*xpath_selectors)

    def _descendant(self, parent, element_names):
        if len(element_names) == 1:
            return "{0}//{1}".format(parent, element_names[0])
        elif len(element_names) > 1:
            element_names_xpath = " | ".join(["self::{0}".format(e) for e in element_names])
            return "{0}//*[{1}]".format(parent, element_names_xpath)
        else:
            return "{0}//*".format(parent)

    def _equality(self, expr1, expr2):
        return "{0} = {1}".format(expr1, expr2)

    def _inverse(self, expr):
        return "not({0})".format(expr)

    def _is(self, expr1, expr2):
        if self.exact:
            return self._equality(expr1, expr2)
        else:
            return self._contains(expr1, expr2)

    def _next_sibling(self, current, element_names):
        if len(element_names) == 1:
            return "{0}/following-sibling::*[1]/self::{1}".format(current, element_names[0])
        elif len(element_names) > 1:
            element_names_xpath = " | ".join(["self::{0}".format(e) for e in element_names])
            return "{0}/following-sibling::*[1]/self::*[{1}]".format(current, element_names_xpath)
        else:
            return "{0}/following-sibling::*[1]/self::*".format(current)

    def _node_name(self, current):
        return "name({0})".format(current)

    def _normalized_space(self, expr):
        return "normalize-space({0})".format(expr)

    def _one_of(self, expr, *values):
        return " or ".join(["{0} = {1}".format(expr, value) for value in values])

    def _or(self, *exprs):
        return "({0})".format(" or ".join(exprs))

    def _previous_sibling(self, current, element_names):
        if len(element_names) == 1:
            return "{0}/preceding-sibling::*[1]/self::{1}".format(current, element_names[0])
        elif len(element_names) > 1:
            element_names_xpath = " | ".join(["self::{0}".format(e) for e in element_names])
            return "{0}/preceding-sibling::*[1]/self::*[{1}]".format(current, element_names_xpath)
        else:
            return "{0}/preceding-sibling::*[1]/self::*".format(current)

    def _starts_with(self, current, expr):
        return "starts-with({0}, {1})".format(current, expr)

    def _string_function(self, expr):
        return "string({0})".format(expr)

    def _string_length_function(self, current):
        return "string-length({0})".format(current)

    def _string_literal(self, string):
        string = _ensure_string(string)

        def wrap(s):
            return "'{0}'".format(s)

        if "'" in string:
            parts = string.split("'")
            parts = map(wrap, parts)

            return "concat(" + ",\"'\",".join(parts) + ")"
        else:
            return wrap(string)

    def _substring_function(self, current, start, length=None):
        args = [start]
        if length is not None:
            args.append(length)
        return "substring({0}, {1})".format(current, ", ".join(args))

    def _text(self, current):
        return "{0}/text()".format(current)

    def _this_node(self):
        return "."

    def _union(self, *exprs):
        return " | ".join(exprs)

    def _where(self, expr, *predicate_exprs):
        predicates = ["[{0}]".format(predicate_expr) for predicate_expr in predicate_exprs]
        return "{0}{1}".format(expr, "".join(predicates))


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


if sys.version_info >= (3, 0):
    def _is_string(argument):
        return isinstance(argument, (str, bytes))

    def _ensure_string(string):
        return string.decode("UTF-8") if isinstance(string, bytes) else string
else:
    def _is_string(argument):
        return isinstance(argument, (str, unicode))

    def _ensure_string(string):
        return string.encode("UTF-8") if isinstance(string, unicode) else string


_selector_to_xpath = partial(HTMLTranslator().selector_to_xpath, prefix=None)
