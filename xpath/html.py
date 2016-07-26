"""
A set of XPath query generators for matching semantic HTML elements.
"""

from xpath.renderer import (
    attribute,
    descendant,
    equality,
    is_,
    normalized_space,
    one_of,
    or_,
    string_literal,
    this_node,
    union,
    where)


def button(locator, exact=False):
    """
    Returns an XPath query for finding buttons matching the given locator.

    The query defines a button as one of the following:
    * a `button` element
    * an `input` element with a `type` of "button"
    * an `input` element with a `type` of "image"
    * an `input` element with a `type` of "reset"
    * an `input` element with a `type` of "submit"

    The query will match buttons that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element `value` matches the locator
    * the element `title` matches the locator
    * the element text matches the locator
    * the element `alt` of an "image" `input` element matches the locator

    Args:
        locator (str): A string that identifies the desired buttons.
        exact (bool, optional): Whether the query should perform an exact match with the given
            locator. Defaults to False.

    Returns:
        str: An XPath query matching the desired buttons.
    """

    return union(
        where(
            descendant(this_node(), "button"),
            or_(
                equality(
                    attribute(this_node(), "id"),
                    string_literal(locator)),
                is_(
                    attribute(this_node(), "value"),
                    string_literal(locator),
                    exact=exact),
                is_(
                    attribute(this_node(), "title"),
                    string_literal(locator),
                    exact=exact),
                is_(
                    normalized_space(this_node()),
                    string_literal(locator),
                    exact=exact))),
        where(
            descendant(this_node(), "input"),
            one_of(
                attribute(this_node(), "type"),
                [string_literal("button"),
                 string_literal("image"),
                 string_literal("reset"),
                 string_literal("submit")]),
            or_(
                equality(
                    attribute(this_node(), "id"),
                    string_literal(locator)),
                is_(
                    attribute(this_node(), "value"),
                    string_literal(locator),
                    exact=exact),
                is_(
                    attribute(this_node(), "title"),
                    string_literal(locator),
                    exact=exact))),
        where(
            descendant(this_node(), "input"),
            equality(
                attribute(this_node(), "type"),
                string_literal("image")),
            is_(
                attribute(this_node(), "alt"),
                string_literal(locator),
                exact=exact)))
