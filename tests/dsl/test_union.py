from tests.case import DSLTestCase
from xpath.dsl import attr, descendant
from xpath.renderer import to_xpath


class TestUnion(DSLTestCase):
    __fixture__ = "simple.html"

    def test_creates_a_union_expression(self):
        expr1 = descendant("p")
        expr2 = descendant("div")

        collection = expr1.union(expr2)

        xpath1 = to_xpath(collection.where(attr("id").equals("union-item-3")))
        xpath2 = to_xpath(collection.where(attr("id").equals("union-item-4")))

        results = self.find_all(xpath1)
        self.assertEqual(results[0].text, "Cherry")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].text, "Date")

    def test_aliased_as_plus_sign(self):
        expr1 = descendant("p")
        expr2 = descendant("div")

        collection = expr1 + expr2

        xpath1 = to_xpath(collection.where(attr("id").equals("union-item-3")))
        xpath2 = to_xpath(collection.where(attr("id").equals("union-item-4")))

        results = self.find_all(xpath1)
        self.assertEqual(results[0].text, "Cherry")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].text, "Date")

    def test_where_aliased_as_square_brackets(self):
        expr1 = descendant("p")
        expr2 = descendant("div")

        collection = expr1.union(expr2)

        xpath1 = to_xpath(collection[attr("id").equals("union-item-3")])
        xpath2 = to_xpath(collection[attr("id").equals("union-item-4")])

        results = self.find_all(xpath1)
        self.assertEqual(results[0].text, "Cherry")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].text, "Date")

    def test_used_as_an_expression(self):
        parent = descendant("div")[attr("id").equals("union")]

        expr1 = descendant("p")
        expr2 = descendant("div")

        collection = expr1.union(expr2)

        xpath1 = to_xpath(parent.descendant(collection[attr("id").equals("union-item-3")]))
        xpath2 = to_xpath(parent.descendant(collection[attr("id").equals("union-item-4")]))

        results = self.find_all(xpath1)
        self.assertEqual(results[0].text, "Cherry")

        results = self.find_all(xpath2)
        self.assertEqual(results[0].text, "Date")

    def test_creates_a_second_order_union(self):
        expr1 = descendant("p")
        expr2 = descendant("div")
        expr3 = descendant("span")

        collection1 = expr1.union(expr2)[attr("id") == "union-item-5"]
        collection2 = collection1.union(expr3[attr("id") == "union-item-6"])

        xpath = to_xpath(collection2)

        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Fig")

    def test_second_order_union_aliased_as_plus_sign(self):
        expr1 = descendant("p")
        expr2 = descendant("div")
        expr3 = descendant("span")

        collection1 = (expr1 + expr2)[attr("id") == "union-item-5"]
        collection2 = collection1 + expr3[attr("id") == "union-item-6"]

        xpath = to_xpath(collection2)

        results = self.find_all(xpath)
        self.assertEqual(results[0].text, "Fig")
