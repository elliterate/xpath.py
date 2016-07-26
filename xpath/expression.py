from enum import Enum
from xpath.literal import Literal


class ExpressionKind(Enum):
    ATTR = "ATTR"
    CONTAINS = "CONTAINS"
    DESCENDANT = "DESCENDANT"
    EQUALITY = "EQUALITY"
    IS = "IS"
    NORMALIZED_SPACE = "NORMALIZED_SPACE"
    ONE_OF = "ONE_OF"
    OR = "OR"
    STRING = "STRING"
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

    def __eq__(self, expression):
        return self.equals(expression)

    def __getitem__(self, expression):
        return self.where(expression)

    def __or__(self, expression):
        return self.or_(expression)

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

    def descendant(self, element_name):
        """
        Returns an expression representing any descendants of the current node (represented by the
        current expression) with the given element name.

        Args:
            element_name (str): The name of the descendant elements to match.

        Returns:
            Expression: A new `Expression` representing the matched descendant nodes.
        """

        return Expression(ExpressionKind.DESCENDANT, self.current, Literal(element_name))

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

    @property
    def string(self):
        """
        Returns an expression representing the string contents of this one.

        Returns:
            Expression: A new `Expression` representing the string contents of this one.
        """

        return Expression(ExpressionKind.STRING, self.current)

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
