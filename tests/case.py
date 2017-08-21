import inspect
from lxml import etree
import os
import pytest
import unittest
from xpath import html
from xpath.renderer import to_xpath


_TEST_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
_FIXTURE_DIR = os.path.join(_TEST_DIR, "fixtures")


class TestCase(unittest.TestCase):
    """A base test case for testing XPath queries."""

    __fixture__ = None
    """str: The name of the HTML fixture file against which to run all XPath queries."""

    @pytest.fixture(autouse=True)
    def setup_document(self):
        # Determine the path of the fixture to load.
        filename = getattr(type(self), "__fixture__")
        fixture_path = os.path.join(_FIXTURE_DIR, filename)

        parser = etree.HTMLParser(encoding="UTF-8")

        # Open the fixture file in the browser.
        self.document = etree.parse(fixture_path, parser)


class DSLTestCase(TestCase):
    def find_all(self, xpath):
        """
        Returns all elements matching the given XPath query.

        Args:
            xpath (str): An XPath query to match.

        Returns:
            list(WebElement): A list of matching `WebElement` objects.
        """

        return self.document.xpath(xpath)


class HTMLTestCase(TestCase):
    """A base test case for testing HTML matchers."""

    __matcher__ = None
    """str: The name of the matcher in the `xpath.html` module to use for locating elements."""

    def get(self, locator, exact=False):
        """
        Returns the `data` attribute of the first element matching the locator, if any.

        Args:
            locator (str): A string that identifies the desired element.

        Returns:
            str | None: The `data` attribute of the first matching element, if any.
        """

        # Determine the `xpath.html` matcher.
        matcher_name = getattr(type(self), "__matcher__")
        matcher = getattr(html, matcher_name)

        # Find all matching elements.
        expression = matcher(locator)
        xpath = to_xpath(expression, exact=exact)
        elements = self.document.xpath(xpath)

        return elements[0].get("data") if len(elements) else None
