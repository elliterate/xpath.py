import inspect
import os
import pytest
import unittest
from xpath import html


_TEST_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
_FIXTURE_DIR = os.path.join(_TEST_DIR, "fixtures")


class TestCase(unittest.TestCase):
    """A base test case for testing XPath queries."""

    __fixture__ = None
    """str: The name of the HTML fixture file against which to run all XPath queries."""

    @pytest.fixture(autouse=True)
    def setup_driver(self, driver):
        self.driver = driver

        # Determine the path of the fixture to load.
        filename = getattr(type(self), "__fixture__")
        fixture_path = os.path.join(_FIXTURE_DIR, filename)

        # Open the fixture file in the browser.
        self.driver.get("file://{0}".format(fixture_path))


class DSLTestCase(TestCase):
    def find_all(self, xpath):
        """
        Returns all elements matching the given XPath query.

        Args:
            xpath (str): An XPath query to match.

        Returns:
            list(WebElement): A list of matching `WebElement` objects.
        """

        return self.driver.find_elements_by_xpath(xpath)


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
        xpath = matcher(locator, exact=exact)
        elements = self.driver.find_elements_by_xpath(xpath)

        return elements[0].get_attribute("data") if len(elements) else None
