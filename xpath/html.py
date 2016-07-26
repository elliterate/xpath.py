"""
A set of `Expression` generators for matching semantic HTML elements.
"""

from xpath.dsl import anywhere, attr, descendant, string


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


def checkbox(locator):
    """
    Returns an `Expression` for finding checkboxes matching the given locator.

    The query will match checkboxes that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element `name` exactly matches the locator
    * the element `id` exactly matches the `for` attribute of a corresponding `label` element
      whose text matches the locator
    * the element is nested within a `label` element whose text matches the locator

    Args:
        locator (str): A string that identifies the desired checkboxes.

    Returns:
        Expression: An `Expression` object matching the desired checkboxes.
    """

    base_expr = descendant("input")[attr("type").equals("checkbox")]

    expr = base_expr[
        attr("id").equals(locator) |
        attr("name").equals(locator) |
        attr("id").equals(anywhere("label")[string.n.is_(locator)].attr("for"))]
    expr += descendant("label")[string.n.is_(locator)].descendant(base_expr)

    return expr


def link(locator):
    """
    Returns an `Expression` for finding links matching the given locator.

    The query defines a link as an `a` element with an `href` attribute and will match links that
    meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element `title` matches the locator
    * the element text matches the locator
    * the `alt` of a nested `img` element matches the locator

    Args:
        locator (str): A string that identifies the desired links.

    Returns:
        Expression: An `Expression` object matching the desired links.
    """

    expr = descendant("a")[attr("href")][
        attr("id").equals(locator) |
        attr("title").is_(locator) |
        string.n.is_(locator) |
        descendant("img")[attr("alt").is_(locator)]]

    return expr
