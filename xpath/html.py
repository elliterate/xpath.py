"""
A set of `Expression` generators for matching semantic HTML elements.
"""

from xpath.dsl import attr, descendant, string


def button(locator):
    """
    Returns an `Expression` for finding buttons matching the given locator.

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

    Returns:
        Expression: An `Expression` object matching the desired buttons.
    """

    expr = descendant("button")[
        attr("id").equals(locator) |
        attr("value").is_(locator) |
        attr("title").is_(locator) |
        string.n.is_(locator)]
    expr += descendant("input")[attr("type").one_of("submit", "reset", "image", "button")][
        attr("id").equals(locator) |
        attr("value").is_(locator) |
        attr("title").is_(locator) |
        string.n.is_(locator)]
    expr += descendant("input")[attr("type").equals("image")][attr("alt").is_(locator)]

    return expr
