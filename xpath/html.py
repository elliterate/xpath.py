"""
A set of `Expression` generators for matching semantic HTML elements.
"""

from xpath.dsl import anywhere, attr, child, descendant, previous_sibling, string


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

    field_expr = descendant("input")[attr("type").equals("checkbox")]
    return _locate_field(field_expr, locator)


def definition_description(locator):
    """
    Returns an `Expression` for finding definition descriptions matching the given locator.

    The query will match definition descriptions that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element immediately follows a sibling `dt` whose text matches the locator

    Args:
        locator (str): A string that identifies the desired definition descriptions.

    Returns:
        Expression: An `Expression` object matching the desired definition descriptions.
    """

    expr = descendant("dd")[
        attr("id").equals(locator) |
        previous_sibling("dt")[string.n.equals(locator)]]

    return expr


def field(locator):
    """
    Returns an `Expression` for finding form fields matching the given locator.

    The query defines a form field as one of the following:
    * an `input` element whose `type` is neither "hidden", "image", nor "submit"
    * a `select` element
    * a `textarea` element

    The query will match form fields that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element `name` exactly matches the locator
    * the element `placeholder` exactly matches the locator
    * the element `id` exactly matches the `for` attribute of a corresponding `label` element
      whose text matches the locator
    * the element is nested within a `label` element whose text matches the locator

    Args:
        locator (str): A string that identifies the desired form fields.
    Return:
        Expression: An `Expression` object matching the desired form fields.
    """

    field_expr = descendant("input", "select", "textarea")[
        ~attr("type").one_of("hidden", "image", "submit")]
    return _locate_field(field_expr, locator)


def fieldset(locator):
    """
    Returns an `Expression` for finding fieldsets matching the given locator.

    The query will match fieldsets that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element has a child `legend` element whose text matches the locator

    Args:
        locator (str): A string that identifies the desired fieldsets.

    Returns:
        Expression: An `Expression` object matching the desired fieldsets.
    """

    expr = descendant("fieldset")[
        attr("id").equals(locator) |
        child("legend")[string.n.is_(locator)]]

    return expr


def file_field(locator):
    """
    Returns an `Expression` for finding file fields matching the given locator.

    The query will match file fields that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element `name` exactly matches the locator
    * the element `id` exactly matches the `for` attribute of a corresponding `label` element
      whose text matches the locator
    * the element is nested within a `label` element whose text matches the locator

    Args:
        locator (str): A string that identifies the desired file fields.

    Returns:
        Expression: An `Expression` object matching the desired file fields.
    """

    field_expr = descendant("input")[attr("type").equals("file")]
    return _locate_field(field_expr, locator)


def fillable_field(locator):
    """
    Returns an `Expression` for finding fillable fields matching the given locator.

    The query defines a fillable field as one of the following:
    * an `input` element whose `type` is neither "checkbox", "file", "hidden", "image", "radio",
      nor "submit"
    * a `textarea` element

    The query will match fillable fields that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element `name` exactly matches the locator
    * the element `placeholder` exactly matches the locator
    * the element `id` exactly matches the `for` attribute of a corresponding `label` element
      whose text matches the locator
    * the element is nested within a `label` element whose text matches the locator

    Args:
        locator (str): A string that identifies the desired fillable fields.

    Returns:
        Expression: An `Expression` object matching the desired fillable fields.
    """

    field_expr = descendant("input", "textarea")[
        ~attr("type").one_of("checkbox", "file", "hidden", "image", "radio", "submit")]
    return _locate_field(field_expr, locator)


def frame(locator):
    """
    Returns an `Expression` for finding frames matching the given locator.

    The query defines a frame as one of the following:
    * a `frame` element
    * an `iframe` element

    The query will match frames that meet one of the following criteria:
    * the element `id` exactly matches the locator
    * the element `name` exactly matches the locator

    Args:
        locator (str): A string that identifies the desired frames.

    Returns:
        Expression: An `Expression` object matching the desired frames.
    """

    frames = descendant("frame") + descendant("iframe")
    return frames[attr("id").equals(locator) | attr("name").equals(locator)]


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


def link_or_button(locator):
    """
    Returns an `Expression` for finding links or buttons matching the given locator.

    See the `link` and `button` methods for more information on what they match.

    Args:
        locator (str): A string that identifies the desired links and buttons.

    Returns:
        Expression: An `Expression` object matching the desired links and buttons.
    """

    return link(locator) + button(locator)


def optgroup(locator):
    """
    Returns an `Expression` for finding option groups matching the given locator.

    The query will match option groups whose `label` matches the locator.

    Args:
        locator (str): A string that identifies the desired option groups.

    Returns:
        Expression: An `Expression` object matching the desired option groups.
    """

    expr = descendant("optgroup")[attr("label").is_(locator)]
    return expr


def option(locator):
    """
    Returns an `Expression` for finding options matching the given locator.

    The query will match options whose text matches the locator.

    Args:
        locator (str): A string that identifies the desired options.

    Returns:
        Expression: An `Expression` object matching the desired options.
    """

    expr = descendant("option")[string.n.is_(locator)]
    return expr


def radio_button(locator):
    """
    Returns an `Expression` for finding radio buttons matching the given locator.

    The query will match radio buttons that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element `name` exactly matches the locator
    * the element `id` exactly matches the `for` attribute of a corresponding `label` element
      whose text matches the locator
    * the element is nested within a `label` element whose text matches the locator

    Args:
        locator (str): A string that identifies the desired radio buttons.

    Returns:
        Expression: An `Expression` object matching the desired radio buttons.
    """

    field_expr = descendant("input")[attr("type").equals("radio")]
    return _locate_field(field_expr, locator)


def select(locator):
    """
    Returns an `Expression` for finding selects matching the given locator.

    The query will match selects that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element `name` exactly matches the locator
    * the element `id` exactly matches the `for` attribute of a corresponding `label` element
      whose text matches the locator
    * the element is nested within a `label` element whose text matches the locator

    Args:
        locator (str): A string that identifies the desired selects.

    Returns:
        Expression: An `Expression` object matching the desired selects.
    """

    field_expr = descendant("select")
    return _locate_field(field_expr, locator)


def table(locator):
    """
    Returns an `Expression` for finding tables matching the given locator.

    The query will match tables that meet at least one of the following criteria:
    * the element `id` exactly matches the locator
    * the element has a descendant `caption` element whose text matches the locator

    Args:
        locator (str): A string that identifies the desired tables.

    Returns:
        Expression: An `Expression` object matching the desired tables.
    """

    expr = descendant("table")[
        attr("id").equals(locator) |
        descendant("caption").is_(locator)]

    return expr


def _locate_field(field_expr, locator):
    expr = field_expr[
        attr("id").equals(locator) |
        attr("name").equals(locator) |
        attr("placeholder").equals(locator) |
        attr("id").equals(anywhere("label")[string.n.is_(locator)].attr("for"))]
    expr += descendant("label")[string.n.is_(locator)].descendant(field_expr)

    return expr
