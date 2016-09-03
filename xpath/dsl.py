"""
A set of `Expression` generators relative to the current expression context, i.e., `.`.
"""

from xpath.expression import Expression, ExpressionKind
from xpath.literal import Literal


current = Expression(ExpressionKind.THIS_NODE)

anywhere = current.anywhere
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
