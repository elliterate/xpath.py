"""
A set of `Expression` generators relative to the current expression context, i.e., `.`.
"""

from xpath.expression import Expression, ExpressionKind


current = Expression(ExpressionKind.THIS_NODE)

attr = current.attr
descendant = current.descendant
string = current.string
