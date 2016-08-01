from enum import Enum
from xpath.literal import Literal


class ExpressionKind(Enum):
    AND = "AND"
    ANYWHERE = "ANYWHERE"
    ATTR = "ATTR"
    CHILD = "CHILD"
    CONTAINS = "CONTAINS"
    DESCENDANT = "DESCENDANT"
    EQUALITY = "EQUALITY"
    INVERSE = "INVERSE"
    IS = "IS"
    NODE_NAME = "NODE_NAME"
    NORMALIZED_SPACE = "NORMALIZED_SPACE"
    ONE_OF = "ONE_OF"
    OR = "OR"
    PREVIOUS_SIBLING = "PREVIOUS_SIBLING"
    STRING = "STRING"
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
            expression (Expression): The test expression that should be exactly matched.

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

    def previous_sibling(self, element_name):
        """
        Returns an expression representing the sibling immediately preceding the element represented
        by the current expression.

        Args:
            element_name (str): The name of the sibling element.

        Returns:
            Expression: A new `Expression` representing the preceding sibling element.
        """

        return Expression(ExpressionKind.PREVIOUS_SIBLING, self.current, Literal(element_name))

    @property
    def string(self):
        """
        Returns an expression representing the string contents of this one.

        Returns:
            Expression: A new `Expression` representing the string contents of this one.
        """

        return Expression(ExpressionKind.STRING, self.current)

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
        Returns an expression for the union of this one and another.

        Args:
            expression (Expression): The right-hand side expression to be united with this one.

        Returns:
            Expression: A new `Expression` representing the union of the two.
        """

        return Expression(ExpressionKind.UNION, self.current, expression)

    def where(self, expression):
        """
        Returns an expression that applies another expression as a filtering predicate of this one.

        Args:
            expression (Expression): The predicate expression that should filter this one.

        Returns:
            Expression: A new `Expression` representing the filtered expression.
        """

        return Expression(ExpressionKind.WHERE, self.current, expression)
