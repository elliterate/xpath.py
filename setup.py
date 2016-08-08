import os
from setuptools import setup, find_packages
import sys


install_requires = ["cssselect"]
if sys.version_info < (3, 4):
    install_requires.append("enum34")


def read(filename):
    """Returns the contents of the given package file."""

    path = os.path.join(os.path.dirname(__file__), filename)

    with open(path) as f:
        return f.read()


def get_version():
    """Returns the package version."""

    global_vars = {}

    # Compile and execute the individual file to prevent
    # the package from being automatically loaded.
    source = read(os.path.join("xpath", "version.py"))
    code = compile(source, "version.py", "exec")
    exec(code, global_vars)

    return global_vars['__version__']


setup(
    name="xpath-py",
    version=get_version(),
    description="Python library for generating XPath expressions",
    long_description=read("README.rst"),
    url="https://github.com/elliterate/xpath.py",
    author="Ian Lesperance",
    author_email="ian@elliterate.com",
    license="MIT",
    keywords="xpath",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: XML",
        "Topic :: Utilities"],
    packages=find_packages(exclude=["tests*"]),
    install_requires=install_requires,
    setup_requires=["pytest-runner"],
    tests_require=[
        "pytest",

        # Prevent the use of Selenium 3 until it compiles.
        # See: https://github.com/SeleniumHQ/selenium/pull/2539
        "selenium < 3"])
