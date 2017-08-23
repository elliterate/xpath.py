from __future__ import unicode_literals

from cssselect import HTMLTranslator, parse
from functools import partial
from xpath.compat import bytes_, str_
from xpath.expression import AbstractExpression, ExpressionType
from xpath.literal import Literal
from xpath.utils import decode_bytes


class Renderer(object):
    """A rendering context for converting an XPath :class:`Expression` into a valid string query."""

    _RENDER_METHOD_NAMES = {
        ExpressionType.ANYWHERE: "_anywhere",
        ExpressionType.ATTR: "_attribute",
        ExpressionType.AXIS: "_axis",
        ExpressionType.BINARY_OPERATOR: "_binary_operator",
        ExpressionType.CHILD: "_child",
        ExpressionType.CSS: "_css",
        ExpressionType.DESCENDANT: "_descendant",
        ExpressionType.FUNCTION: "_function",
        ExpressionType.IS: "_is",
        ExpressionType.TEXT: "_text",
        ExpressionType.THIS_NODE: "_this_node",
        ExpressionType.UNION: "_union",
        ExpressionType.WHERE: "_where",
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
        Converts a given XPath :class:`Expression` into a corresponding string query.

        Args:
            node (Expression): An XPath :class:`Expression` to convert.

        Returns:
            str: A valid XPath query corresponding to the given :class:`Expression`.
        """

        args = [self._convert_argument(arg) for arg in node.arguments]
        render_method_name = self._RENDER_METHOD_NAMES[node.type]
        render_method = getattr(self, render_method_name)
        return render_method(*args)

    def _convert_argument(self, argument):
        if isinstance(argument, AbstractExpression):
            return self.render(argument)
        if isinstance(argument, list):
            return [self._convert_argument(element) for element in argument]
        if isinstance(argument, int):
            return str(argument)
        if isinstance(argument, (bytes_, str_)):
            return self._string_literal(argument)
        if isinstance(argument, Literal):
            return argument.value

    @classmethod
    def _anywhere(cls, element_names):
        return cls._with_element_conditions("//", element_names)

    @staticmethod
    def _attribute(node, attribute_name):
        return "{node}/@{attribute_name}".format(node=node, attribute_name=attribute_name)

    @classmethod
    def _axis(cls, current, name, element_names):
        return cls._with_element_conditions(
            "{current}/{axis}::".format(current=current, axis=name), element_names)

    @staticmethod
    def _binary_operator(name, left, right):
        return "({left} {operator} {right})".format(left=left, operator=name, right=right)

    @classmethod
    def _child(cls, parent, element_names):
        return cls._with_element_conditions("{parent}/".format(parent=parent), element_names)

    @classmethod
    def _css(cls, current, css_selector):
        # The given CSS selector may be a group selector (multiple selectors
        # delimited by commas), so we must parse out and convert the individual
        # selectors, then return their union.
        selectors = parse(css_selector)
        xpath_selectors = ["{current}//{selector}".format(current=current,
                                                          selector=_selector_to_xpath(selector))
                           for selector in selectors]
        return cls._union(*xpath_selectors)

    @classmethod
    def _descendant(cls, parent, element_names):
        return cls._with_element_conditions("{parent}//".format(parent=parent), element_names)

    @staticmethod
    def _function(name, *arguments):
        return "{function}({arguments})".format(function=name, arguments=", ".join(arguments))

    def _is(self, expr1, expr2):
        if self.exact:
            return self._binary_operator("=", expr1, expr2)
        else:
            return self._function("contains", expr1, expr2)

    @staticmethod
    def _string_literal(string):
        string = decode_bytes(string)

        def wrap(s):
            return "'{}'".format(s)

        if "'" in string:
            parts = string.split("'")
            parts = map(wrap, parts)

            return "concat(" + ",\"'\",".join(parts) + ")"
        else:
            return wrap(string)

    @staticmethod
    def _text(current):
        return "{current}/text()".format(current=current)

    @staticmethod
    def _this_node():
        return "."

    @staticmethod
    def _union(*exprs):
        return " | ".join(exprs)

    @staticmethod
    def _where(expr, *predicate_exprs):
        predicates_xpath = ["[{predicate}]".format(predicate=predicate_expr)
                      for predicate_expr in predicate_exprs]
        return "{expression}{predicates}".format(
            expression=expr, predicates="".join(predicates_xpath))

    @staticmethod
    def _with_element_conditions(expression, element_names):
        if len(element_names) == 1:
            return "{expression}{element_name}".format(expression=expression,
                                                       element_name=element_names[0])
        elif len(element_names) > 1:
            element_names_xpath = " | ".join(
                ["self::{element_name}".format(element_name=element_name)
                 for element_name in element_names])
            return "{expression}*[{element_names}]".format(expression=expression,
                                                           element_names=element_names_xpath)
        else:
            return "{expression}*".format(expression=expression)


def to_xpath(node, exact=False):
    """
    Converts a given XPath :class:`Expression` into a corresponding string query.

    Args:
        node (Expression): An XPath :class:`Expression` to convert.
        exact (bool, optional): Whether the generated query should perform exact or approximate
            locator matches. Defaults to False.

    Returns:
        str: A valid XPath query corresponding to the given :class:`Expression`.
    """

    return Renderer(exact=exact).render(node)


_selector_to_xpath = partial(HTMLTranslator().selector_to_xpath, prefix=None)
