class Literal(object):
    """
    A literal value that should not be escaped when used in an XPath query.
    """

    def __init__(self, value):
        """
        Args:
            value (str): The raw value.
        """

        self.value = value
