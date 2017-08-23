from lxml import etree


def inner_text(node):
    """
    Returns the inner text of a given XML node, excluding tags.

    Args:
        node (lxml.etree.Element): The node whose inner text is desired.

    Returns:
        str: The inner text of the node.
    """

    # Include text content at the start of the node.
    parts = [node.text]

    for child in node.getchildren():
        # Include the raw text content of the child.
        parts.append(etree.tostring(child, encoding="unicode", method="text"))

        # Include any text following the child.
        parts.append(child.tail)

    # Discard any non-existent text parts and return.
    return "".join(filter(None, parts))
