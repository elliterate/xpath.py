"""
A set of :class:`Expression` generators relative to the current expression context, i.e., ``.``.
"""

from xpath.expression import Expression, ExpressionType, function


current = Expression(ExpressionType.THIS_NODE)

ancestor = current.ancestor
anywhere = current.anywhere
attr = current.attr
axis = current.axis
child = current.child
contains = current.contains
count = current.count
css = current.css
descendant = current.descendant
following_sibling = current.following_sibling
method = current.method
name = current.name
next_sibling = current.next_sibling
preceding_sibling = current.preceding_sibling
previous_sibling = current.previous_sibling
starts_with = current.starts_with
string = current.string
string_length = current.string_length
substring = current.substring
text = current.text


def last():
    return function("last")


def position():
    return function("position")
