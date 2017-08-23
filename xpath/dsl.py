"""
A set of :class:`Expression` generators relative to the current expression context, i.e., ``.``.
"""

from xpath.expression import Expression, ExpressionKind
from xpath.literal import Literal


current = Expression(ExpressionKind.THIS_NODE)

anywhere = current.anywhere
attr = current.attr
axis = current.axis
child = current.child
contains = current.contains
count = current.count
css = current.css
descendant = current.descendant
function = current.function
last = current.last
method = current.method
name = current.name
next_sibling = current.next_sibling
position = current.position
previous_sibling = current.previous_sibling
starts_with = current.starts_with
string = current.string
string_length = current.string_length
substring = current.substring
text = current.text
