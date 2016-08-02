"""
A set of `Expression` generators relative to the current expression context, i.e., `.`.
"""

from xpath.expression import Expression, ExpressionKind
from xpath.literal import Literal


current = Expression(ExpressionKind.THIS_NODE)

attr = current.attr
axis = current.axis
child = current.child
contains = current.contains
css = current.css
descendant = current.descendant
name = current.name
next_sibling = current.next_sibling
previous_sibling = current.previous_sibling
starts_with = current.starts_with
string = current.string
string_length = current.string_length
substring = current.substring
text = current.text


def anywhere(element_name):
    """
    Returns an `Expression` matching nodes with the given element name anywhere in the document.

    Args:
        element_name (str): The name of the elements to match.

    Returns:
        Expression: An `Expression` representing the matched elements.
    """

    return Expression(ExpressionKind.ANYWHERE, Literal(element_name))
