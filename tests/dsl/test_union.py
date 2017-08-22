from tests.case import DSLTestCase
from xpath import dsl as x
from xpath.renderer import to_xpath


class TestUnion(DSLTestCase):
    __fixture__ = "simple.html"

    def test_creates_a_union_expression(self):
        expr1 = x.descendant("p")
        expr2 = x.descendant("div")

        collection = expr1.union(expr2)

        xpath1 = to_xpath(collection.where(x.attr("id").equals("union-item-3")))
        xpath2 = to_xpath(collection.where(x.attr("id").equals("union-item-4")))

        results = self.find_all(xpath1)
        self.assertEqual(results[0].text, "Cherry")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].text, "Date")

    def test_aliased_as_plus_sign(self):
        expr1 = x.descendant("p")
        expr2 = x.descendant("div")

        collection = expr1 + expr2

        xpath1 = to_xpath(collection.where(x.attr("id").equals("union-item-3")))
        xpath2 = to_xpath(collection.where(x.attr("id").equals("union-item-4")))

        results = self.find_all(xpath1)
        self.assertEqual(results[0].text, "Cherry")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].text, "Date")

    def test_where_aliased_as_square_brackets(self):
        expr1 = x.descendant("p")
        expr2 = x.descendant("div")

        collection = expr1.union(expr2)

        xpath1 = to_xpath(collection[x.attr("id").equals("union-item-3")])
        xpath2 = to_xpath(collection[x.attr("id").equals("union-item-4")])

        results = self.find_all(xpath1)
        self.assertEqual(results[0].text, "Cherry")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].text, "Date")

    def test_used_as_an_expression(self):
        parent = x.descendant("div")[x.attr("id").equals("union")]

        expr1 = x.descendant("p")
        expr2 = x.descendant("div")

        collection = expr1.union(expr2)

        xpath1 = to_xpath(parent.descendant(collection[x.attr("id").equals("union-item-3")]))
        xpath2 = to_xpath(parent.descendant(collection[x.attr("id").equals("union-item-4")]))

        results = self.find_all(xpath1)
        self.assertEqual(results[0].text, "Cherry")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].text, "Date")

    def test_creates_a_second_order_union(self):
        expr1 = x.descendant("p")
        expr2 = x.descendant("div")
        expr3 = x.descendant("span")

        collection1 = expr1.union(expr2)[x.attr("id") == "union-item-5"]
        collection2 = collection1.union(expr3[x.attr("id") == "union-item-6"])

        xpath = to_xpath(collection2)

        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Fig")

    def test_second_order_union_aliased_as_plus_sign(self):
        expr1 = x.descendant("p")
        expr2 = x.descendant("div")
        expr3 = x.descendant("span")

        collection1 = (expr1 + expr2)[x.attr("id") == "union-item-5"]
        collection2 = collection1 + expr3[x.attr("id") == "union-item-6"]

        xpath = to_xpath(collection2)

        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Fig")
