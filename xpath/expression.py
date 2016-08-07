from enum import Enum
from xpath.literal import Literal


class ExpressionKind(Enum):
    AND = "AND"
    ANYWHERE = "ANYWHERE"
    ATTR = "ATTR"
    AXIS = "AXIS"
    CHILD = "CHILD"
    CONTAINS = "CONTAINS"
    CSS = "CSS"
    DESCENDANT = "DESCENDANT"
    EQUALITY = "EQUALITY"
    INVERSE = "INVERSE"
    IS = "IS"
    NEXT_SIBLING = "NEXT_SIBLING"
    NODE_NAME = "NODE_NAME"
    NORMALIZED_SPACE = "NORMALIZED_SPACE"
    ONE_OF = "ONE_OF"
    OR = "OR"
    PREVIOUS_SIBLING = "PREVIOUS_SIBLING"
    STARTS_WITH = "STARTS_WITH"
    STRING = "STRING"
    STRING_LENGTH_FUNCTION = "STRING_LENGTH_FUNCTION"
    SUBSTRING_FUNCTION = "SUBSTRING_FUNCTION"
    TEXT = "TEXT"
    THIS_NODE = "THIS_NODE"
    UNION = "UNION"
    WHERE = "WHERE"


class Expression(object):
    """A representation of an expression that can occur in an XPath query."""

    def __init__(self, kind, *args):
        """
        Args:
            kind (ExpressionKind): The kind of XPath query expression this instance represents.
            *args (list(Expression | Literal | str)): Zero or more arguments for the given XPath
                query expression.
        """

        self.kind = kind
        self.arguments = args

    @property
    def current(self):
        return self

    def __add__(self, expression):
        return self.union(expression)

    def __and__(self, expression):
        return self.and_(expression)

    def __eq__(self, expression):
        return self.equals(expression)

    def __getitem__(self, expression):
        return self.where(expression)

    def __invert__(self):
        return self.inverse

    def __or__(self, expression):
        return self.or_(expression)

    def and_(self, expression):
        """
        Returns an expression for the boolean-AND of this one and another.

        Args:
            expression (Expression): The right-hand side expression to be boolean-AND'd with this
                one.

        Returns:
            Expression: A new `Expression` representing the boolean-AND of the two.
        """

        return Expression(ExpressionKind.AND, self.current, expression)

    def attr(self, attribute_name):
        """
        Returns an expression matching the given attribute of the node represented by this
        expression.

        Args:
            attribute_name: The name of the attribute to match.

        Returns:
            Expression: A new `Expression` representing the desired attribute.
        """

        return Expression(ExpressionKind.ATTR, self.current, Literal(attribute_name))

    def axis(self, axis, element_name="*"):
        """
        Returns an expression matching nodes with a given relationship to this one.

        Args:
            axis (str): The relationship between the current node and the desired node.
            element_name (str, optional): The element name of the desired node. Defaults to "*".

        Returns:
            Expression: A new `Expression` representing the nodes with the desired relationship
                to this one.
        """

        return Expression(ExpressionKind.AXIS, self.current, Literal(axis), Literal(element_name))

    def child(self, expression):
        """
        Returns an expression representing any children of the current node (represented by the
        current expression) that match the given expression or element name.

        Args:
            expression: (Expression | str): An `Expression` or element name representing the
                children to match.

        Returns:
            Expression: A new `Expression` representing the matched child nodes.
        """

        if isinstance(expression, str):
            expression = Literal(expression)

        return Expression(ExpressionKind.CHILD, self.current, expression)

    def contains(self, expression):
        """
        Returns an expression representing whether the content of any nodes (represented by the
        current expression) approximately match the given expression.

        Args:
            expression (Expression): The test expression that should be approximately matched.

        Returns:
            Expression: A new `Expression` representing whether any nodes matched.
        """

        return Expression(ExpressionKind.CONTAINS, self.current, expression)

    def css(self, css_selector):
        """
        Returns an expression representing elements matching the given CSS selector relative to
            the current expression.

        Args:
            css_selector (str): A CSS selector identifying the desired nodes.

        Returns:
            Expression: A new `Expression` representing any matched nodes.
        """

        return Expression(ExpressionKind.CSS, self.current, Literal(css_selector))

    def descendant(self, *expressions):
        """
        Returns an expression representing any descendants of the current node (represented by the
        current expression) that match the given expressions or element names.

        Args:
            *expressions (list(Expression | str)): A list of `Expression` objects or element names
                representing the descendants to match.

        Returns:
            Expression: A new `Expression` representing the matched descendant nodes.
        """

        expressions = [Literal(expression) if isinstance(expression, str) else expression
                       for expression in expressions]

        return Expression(ExpressionKind.DESCENDANT, self.current, expressions)

    def equals(self, expression):
        """
        Returns an expression representing whether the content of any nodes (represented by the
        current expression) exactly match the given expression.

        Args:
            expression (Expression | int): The test expression that should be exactly matched.

        Returns:
            Expression: A new `Expression` representing whether any nodes matched.
        """

        return Expression(ExpressionKind.EQUALITY, self.current, expression)

    @property
    def inverse(self):
        """
        Returns an expression that represents the inverse of this one.

        Returns:
            Expression: A new `Expression` representing the inverse of this one.
        """

        return Expression(ExpressionKind.INVERSE, self.current)

    def is_(self, expression):
        """
        Returns an expression representing whether the content of any nodes (represented by the
        current expression) match the given expression.

        Matching will be either approximate or exact, depending on the configuration of the
        `Renderer` evaluating the returned expression.

        Args:
            expression (Expression): The test expression that should be matched.

        Returns:
            Expression: A new `Expression` representing whether any nodes matched.
        """

        return Expression(ExpressionKind.IS, self.current, expression)

    @property
    def n(self):
        """
        Returns an expression that normalizes the whitespace of this one.

        Returns:
            Expression: A new `Expression` representing the whitespace-normalized expression.
        """

        return Expression(ExpressionKind.NORMALIZED_SPACE, self.current)

    @property
    def name(self):
        """
        Returns an expression that returns the name of the current node.

        Returns:
            Expression: A new `Expression` representing the name of the current node.
        """

        return Expression(ExpressionKind.NODE_NAME, self.current)

    def next_sibling(self, *element_names):
        """
        Returns an expression representing the siblings immediately following the elements
        represented by the current expression.

        Args:
            *element_names (list(str)): A list of the names of sibling elements.

        Returns:
            Expression: A new `Expression` representing the following sibling elements.
        """

        element_names = [Literal(name) for name in element_names]

        return Expression(ExpressionKind.NEXT_SIBLING, self.current, element_names)

    def one_of(self, *values):
        """
        Returns an expression representing whether the current expression equals one of the given
        values.

        Args:
            *values (list(str)): One or more values which the current expression may equal.

        Returns:
            Expression: A new `Expression` representing whether any of the values matched.
        """

        return Expression(ExpressionKind.ONE_OF, self.current, *values)

    def or_(self, expression):
        """
        Returns an expression for the boolean-OR of this one and another.

        Args:
            expression (Expression): The right-hand side expression to be boolean-OR'd with this
                one.

        Returns:
            Expression: A new `Expression` representing the boolean-OR of the two.
        """

        return Expression(ExpressionKind.OR, self.current, expression)

    def previous_sibling(self, *element_names):
        """
        Returns an expression representing the siblings immediately preceding the elements
        represented by the current expression.

        Args:
            *element_names (list(str)): A list of the names of sibling elements.

        Returns:
            Expression: A new `Expression` representing the preceding sibling elements.
        """

        element_names = [Literal(name) for name in element_names]

        return Expression(ExpressionKind.PREVIOUS_SIBLING, self.current, element_names)

    def starts_with(self, expression):
        """
        Returns an expression representing whether the current expression starts with the given
        expression.

        Args:
            expression (Expression | str): An expression with which the current expression should
                begin.

        Returns:
            Expression: A new `Expression` representing whether the current starts with the given.
        """

        return Expression(ExpressionKind.STARTS_WITH, self.current, expression)

    @property
    def string(self):
        """
        Returns an expression representing the string contents of this one.

        Returns:
            Expression: A new `Expression` representing the string contents of this one.
        """

        return Expression(ExpressionKind.STRING, self.current)

    @property
    def string_length(self):
        """
        Returns an expression representing the length of the string contents of this one.

        Returns:
            Expression: A new `Expression` representing the length of the string contents of this
                one.
        """

        return Expression(ExpressionKind.STRING_LENGTH_FUNCTION, self.current)

    def substring(self, start, length=None):
        """
        Returns an expression representing a portion of the string contents of this one.

        Args:
            start (int): The starting index.
            length (int, optional): The length of the substring. Default is None.

        Returns:
            Expression: A new `Expression` representing a portion of the string contents of this
                one.
        """

        assert isinstance(start, int)
        args = [start]

        if length is not None:
            assert isinstance(length, int)
            args.append(length)

        return Expression(ExpressionKind.SUBSTRING_FUNCTION, self.current, *args)

    @property
    def text(self):
        """
        Returns an expression representing the text of this one.

        Returns:
            Expression: A new `Expression` representing the text of this one.
        """

        return Expression(ExpressionKind.TEXT, self.current)

    def union(self, expression):
        """
        Returns the union of this expression and another.

        Args:
            expression (Expression): The right-hand side expression to be united with this one.

        Returns:
            Union: The union of this expression and the other.
        """

        return Union(self.current, expression)

    def where(self, expression):
        """
        Returns an expression that applies another expression as a filtering predicate of this one.

        Args:
            expression (Expression): The predicate expression that should filter this one.

        Returns:
            Expression: A new `Expression` representing the filtered expression.
        """

        return Expression(ExpressionKind.WHERE, self.current, expression)


class Union(object):
    """A representation of the union of two expressions."""

    def __init__(self, *expressions):
        self.kind = ExpressionKind.UNION
        self.expressions = expressions

    @property
    def arguments(self):
        return self.expressions

    def __add__(self, expression):
        return self.union(expression)

    def __getitem__(self, expression):
        return self.where(expression)

    def union(self, expression):
        """
        Returns the union of this expression and another.

        Args:
            expression (Expression): The right-hand side expression to be united with this one.

        Returns:
            Union: The union of this expression and the other.
        """

        return Union(self, expression)

    def where(self, expression):
        """
        Returns a new union where each expression of this one has had the given predicate
        expression applied.

        Args:
            expression (Expression): The predicate expression that should filter the expressions
                in this union.

        Returns:
            Union: A new `Union` representing the filtered expressions.
        """

        return Union(*[expr.where(expression) for expr in self.expressions])
