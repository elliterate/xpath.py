# XPath

XPath is a Python DSL around a subset of XPath 1.0. Its primary purpose is to
facilitate writing complex XPath queries from Python code.

## Generating expressions

To create expressions, use the generators in [`xpath.dsl`](xpath/dsl.py):

``` python
from xpath.dsl import attr, descendant
from xpath.renderer import to_xpath

expression = descendant("ul")[attr("id") == "foo"]
xpath = to_xpath(expression)
```

## HTML

XPath comes with a set of premade XPaths for use with HTML documents.

You can generate these like this:

``` python
from xpath.html import button
from xpath.renderer import to_xpath

to_xpath(button("Save"), exact=True)
```

See [`xpath.html`](xpath/html.py) for all available matchers.

## License

(The MIT License)

Copyright © 2010 Jonas Nicklas

Copyright © 2016 Ian Lesperance

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the ‘Software’), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ‘AS IS’, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
