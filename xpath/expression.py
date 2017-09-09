from enum import Enum
from functools import reduce

from xpath.literal import Literal


class ExpressionType(Enum):
    ANYWHERE = "ANYWHERE"
    ATTR = "ATTR"
    AXIS = "AXIS"
    BINARY_OPERATOR = "BINARY_OPERATOR"
    CHILD = "CHILD"
    CSS = "CSS"
    DESCENDANT = "DESCENDANT"
    FUNCTION = "FUNCTION"
    IS = "IS"
    TEXT = "TEXT"
    THIS_NODE = "THIS_NODE"
    UNION = "UNION"
    WHERE = "WHERE"


def _create_axis(name):
    def func(self, *element_names):
        element_names = [Literal(element_name) for element_name in element_names]

        return Expression(ExpressionType.AXIS, self.current, Literal(name), element_names)

    func.__name__ = name
    func.__doc__ = (
        """
        Returns an expression matching nodes related to this one via the "{axis}" axis.

        Args:
            *element_names (*str): Variable length list of element names of the desired nodes.

        Returns:
            Expression: A new :class:`Expression` representing the nodes related via the "{axis}"
                axis.
        """.format(axis=name))

    return func


def _create_method(name):
    def func(self, *arguments):
        return Expression(ExpressionType.FUNCTION, Literal(name), self, *arguments)

    func.__name__ = name
    func.__doc__ = (
        """
        Returns an expression representing the result of the XPath "{function}" function call with
        the current node as the first argument.

        Args:
            *arguments: Variable length argument list for the XPath function.

        Returns:
            Expression: A new :class:`Expression` representing the result of the function call.
        """.format(function=name))

    return func


def _create_operator(operator):
    def func(self, rhs):
        return Expression(ExpressionType.BINARY_OPERATOR, Literal(operator), self.current, rhs)

    func.__name__ = operator
    func.__doc__ = (
        """
        Returns an expression representing the "{operator}" binary operation with the current
        node and the given right-hand side expression.

        Args:
            rhs (Expression | str | int): The right-hand side expression of the "{operator}"
                operation.

        Returns:
            Expression: A new :class:`Expression` representing the "{operator}" operation.
        """.format(operator=operator))

    return func


class AbstractExpression(object):
    pass


class Expression(AbstractExpression):
    """A representation of an expression that can occur in an XPath query."""

    def __init__(self, type, *args):
        """
        Args:
            type (ExpressionType): The type of XPath query expression this instance represents.
            *args (List[Expression | Literal | str]): Zero or more arguments for the given XPath
                query expression.
        """

        self.type = type
        self.arguments = args

    @property
    def current(self):
        return self

    ancestor = _create_axis("ancestor")
    and_ = __and__ = _create_operator("and")

    def anywhere(self, *element_names):
        """
        Returns an :class:`Expression` matching nodes with the given element name anywhere in the
        document.

        Args:
            *element_names (*str, optional): The names of the elements to match.

        Returns:
            Expression: An :class:`Expression` representing the matched elements.
        """

        return Expression(ExpressionType.ANYWHERE, [Literal(element_name) for element_name in element_names])

    def attr(self, attribute_name):
        """
        Returns an expression matching the given attribute of the node represented by this
        expression.

        Args:
            attribute_name: The name of the attribute to match.

        Returns:
            Expression: A new :class:`Expression` representing the desired attribute.
        """

        return Expression(ExpressionType.ATTR, self.current, Literal(attribute_name))

    def axis(self, axis, *element_names):
        """
        Returns an expression matching nodes with a given relationship to this one.

        Args:
            axis (str): The relationship between the current node and the desired nodes.
            *element_names (*str): Variable length list of element names of the desired nodes.

        Returns:
            Expression: A new :class:`Expression` representing the nodes with the desired
                relationship to this one.
        """

        element_names = [Literal(element_name) for element_name in element_names]

        return Expression(ExpressionType.AXIS, self.current, Literal(axis), element_names)

    def child(self, *expressions):
        """
        Returns an expression representing any children of the current node (represented by the
        current expression) that match the given expression or element name.

        Args:
            *expression (*(Expression | str)): Variable length list of :class:`Expression` objects
                or element names representing the children to match.

        Returns:
            Expression: A new :class:`Expression` representing the matched child nodes.
        """

        expressions = [
            Literal(expression) if isinstance(expression, str) else expression
            for expression in expressions]

        return Expression(ExpressionType.CHILD, self.current, expressions)

    contains = _create_method("contains")
    count = property(_create_method("count"))

    def css(self, css_selector):
        """
        Returns an expression representing elements matching the given CSS selector relative to
            the current expression.

        Args:
            css_selector (str): A CSS selector identifying the desired nodes.

        Returns:
            Expression: A new :class:`Expression` representing any matched nodes.
        """

        return Expression(ExpressionType.CSS, self.current, Literal(css_selector))

    def descendant(self, *expressions):
        """
        Returns an expression representing any descendants of the current node (represented by the
        current expression) that match the given expressions or element names.

        Args:
            *expressions (List[Expression | str]): A list of :class:`Expression` objects or element
                names representing the descendants to match.

        Returns:
            Expression: A new :class:`Expression` representing the matched descendant nodes.
        """

        expressions = [Literal(expression) if isinstance(expression, str) else expression
                       for expression in expressions]

        return Expression(ExpressionType.DESCENDANT, self.current, expressions)

    divide = __truediv__ = __div__ = _create_operator("div")
    following_sibling = _create_axis("following-sibling")
    equals = __eq__ = _create_operator("=")
    gt = __gt__ = _create_operator(">")
    gte = __ge__ = _create_operator(">=")
    inverse = property(_create_method("not"))
    __invert__ = _create_method("not")

    def is_(self, expression):
        """
        Returns an expression representing whether the content of any nodes (represented by the
        current expression) match the given expression.

        Matching will be either approximate or exact, depending on the configuration of the
        :class:`Renderer` evaluating the returned expression.

        Args:
            expression (Expression): The test expression that should be matched.

        Returns:
            Expression: A new :class:`Expression` representing whether any nodes matched.
        """

        return Expression(ExpressionType.IS, self.current, expression)

    lt = __lt__ = _create_operator("<")
    lte = __le__ = _create_operator("<=")

    def method(self, name, *arguments):
        """
        Returns an expression that represents the result of an XPath function call with the current
        node as the first argument.

        Args:
            name (str): The name of the function to call.
            *arguments: Variable length argument list for the XPath function.

        Returns:
            Expression: A new :class:`Expression` representing the result of the function call.
        """

        return Expression(ExpressionType.FUNCTION, Literal(name), self, *arguments)

    minus = _create_operator("-")
    mod = __mod__ = _create_operator("mod")
    multiply = __mul__ = _create_operator("*")
    n = property(_create_method("normalize-space"))
    name = property(_create_method("name"))

    def next_sibling(self, *expressions):
        """
        Returns an expression representing the siblings immediately following the elements
        represented by the current expression.

        Args:
            *expressions (List[str]): A list of expressions representing desired sibling elements.

        Returns:
            Expression: A new :class:`Expression` representing the following sibling elements.
        """

        return self.following_sibling()[1].self_axis(*expressions)

    not_equals = __ne__ = _create_operator("!=")

    def one_of(self, *values):
        """
        Returns an expression representing whether the current expression equals one of the given
        values.

        Args:
            *values (List[str]): One or more values which the current expression may equal.

        Returns:
            Expression: A new :class:`Expression` representing whether any of the values matched.
        """

        return reduce(lambda a, b: a.or_(b), map(self.equals, values))

    or_ = __or__ = _create_operator("or")
    plus = _create_operator("+")
    preceding_sibling = _create_axis("preceding-sibling")

    def previous_sibling(self, *expressions):
        """
        Returns an expression representing the siblings immediately preceding the elements
        represented by the current expression.

        Args:
            *expressions (List[str]): A list of expressions representing desired sibling elements.

        Returns:
            Expression: A new :class:`Expression` representing the preceding sibling elements.
        """

        return self.preceding_sibling()[1].self_axis(*expressions)

    self_axis = _create_axis("self")
    starts_with = _create_method("starts-with")
    string = property(_create_method("string"))
    string_length = property(_create_method("string-length"))
    substring = _create_method("substring")

    @property
    def text(self):
        """
        Returns an expression representing the text of this one.

        Returns:
            Expression: A new :class:`Expression` representing the text of this one.
        """

        return Expression(ExpressionType.TEXT, self.current)

    def union(self, expression):
        """
        Returns the union of this expression and another.

        Args:
            expression (Expression): The right-hand side expression to be united with this one.

        Returns:
            Union: The union of this expression and the other.
        """

        return Union(self.current, expression)

    __add__ = union

    def where(self, expression):
        """
        Returns an expression that applies another expression as a filtering predicate of this one.

        Args:
            expression (Expression): The predicate expression that should filter this one.

        Returns:
            Expression: A new :class:`Expression` representing the filtered expression.
        """

        return Expression(ExpressionType.WHERE, self.current, expression)

    __getitem__ = where


def _create_map(name):
    attr = getattr(Expression, name)

    if isinstance(attr, property):
        def method(expr):
            attr.__getitem__(expr)
    else:
        method = attr

    def map(self, *args, **kwargs):
        return Union(*[method(expr, *args, **kwargs)
                       for expr in self.expressions])

    map.__name__ = name
    map.__doc__ = ("""
        Returns a new union with the :{role}:`Expression.{name}` for each expression of this one.

        Args:
            *args: Variable length argument list for :{role}:`Expression.{name}`.
            **kwargs: Arbitrary keyword arguments for :{role}:`Expression.{name}`.

        Returns:
            Union: A new :class:`Union` representing the mapped expressions.
        """.format(
            role="attr" if isinstance(attr, property) else "meth",
            name=name))

    return map


class Union(AbstractExpression):
    """A representation of the union of two expressions."""

    def __init__(self, *expressions):
        self.type = ExpressionType.UNION
        self.expressions = expressions

    @property
    def arguments(self):
        return self.expressions

    def union(self, expression):
        """
        Returns the union of this expression and another.

        Args:
            expression (Expression): The right-hand side expression to be united with this one.

        Returns:
            Union: The union of this expression and the other.
        """

        return Union(self, expression)

    __add__ = union

    ancestor = _create_map("ancestor")
    and_ = __and__ = _create_map("and_")
    anywhere = _create_map("anywhere")
    attr = _create_map("attr")
    axis = _create_map("axis")
    child = _create_map("child")
    contains = _create_map("contains")
    count = property(_create_map("count"))
    css = _create_map("css")
    descendant = _create_map("descendant")
    divide = __truediv__ = __div__ = _create_map("divide")
    following_sibling = _create_map("following_sibling")
    equals = __eq__ = _create_map("equals")
    gt = __gt__ = _create_map("gt")
    gte = __ge__ = _create_map("gte")
    inverse = property(_create_map("inverse"))
    __invert__ = _create_map("inverse")
    is_ = _create_map("is_")
    lt = __lt__ = _create_map("lt")
    lte = __le__ = _create_map("lte")
    method = _create_map("method")
    minus = _create_map("minus")
    mod = __mod__ = _create_map("mod")
    multiply = __mul__ = _create_map("multiply")
    n = property(_create_map("n"))
    name = property(_create_map("name"))
    next_sibling = _create_map("next_sibling")
    not_equals = __ne__ = _create_map("not_equals")
    one_of = _create_map("one_of")
    or_ = __or__ = _create_map("or_")
    plus = _create_map("plus")
    preceding_sibling = _create_map("preceding_sibling")
    previous_sibling = _create_map("previous_sibling")
    self_axis = _create_map("self_axis")
    starts_with = _create_map("starts_with")
    string = property(_create_map("string"))
    string_length = property(_create_map("string_length"))
    substring = _create_map("substring")
    text = property(_create_map("text"))
    where = __getitem__ = _create_map("where")


def function(name, *arguments):
    """
    Returns an expression that represents the result of the given XPath function.

    Args:
        name (str): The name of the function to call.
        *arguments: Variable length argument list for the function.

    Returns:
        Expression: A new :class:`Expression` representing the result of the function.
    """

    return Expression(ExpressionType.FUNCTION, Literal(name), *arguments)
