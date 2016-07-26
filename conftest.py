import pytest
from selenium import webdriver


@pytest.yield_fixture(scope="session")
def driver():
    driver = webdriver.PhantomJS()
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture(autouse=True)
def reset_driver(driver):
    # Ensure the test does not see any DOM from the previous test.
    driver.get("about:blank")
