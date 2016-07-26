def attribute(node, attribute_name):
    return "{0}/@{1}".format(node, attribute_name)


def contains(expr, value):
    return "contains({0}, {1})".format(expr, value)


def descendant(node, element_name):
    return "{0}//{1}".format(node, element_name)


def equality(expr1, expr2):
    return "{0} = {1}".format(expr1, expr2)


def is_(expr1, expr2, exact=False):
    if exact:
        return equality(expr1, expr2)
    else:
        return contains(expr1, expr2)


def normalized_space(expr):
    return "normalize-space({0})".format(expr)


def one_of(expr, values):
    return " or ".join(["{0} = {1}".format(expr, value) for value in values])


def or_(*exprs):
    return "({0})".format(" or ".join(exprs))


def string_literal(string):
    return "'{0}'".format(string)


def this_node():
    return "."


def union(*exprs):
    return " | ".join(exprs)


def where(expr, *predicate_exprs):
    predicates = ["[{0}]".format(predicate_expr) for predicate_expr in predicate_exprs]
    return "{0}{1}".format(expr, "".join(predicates))
