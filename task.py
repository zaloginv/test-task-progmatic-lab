from itertools import product
from pprint import pprint


def func(num):
    expressions = []

    for p in product(*ls):
        expr = "".join(p)
        if eval(expr) == num:
            expressions.append(expr)

    return {"count": len(expressions),
            "expressions": expressions}


digits = list('9876543210')
signs = ('', '+', '-')

ls = [a + b for (a, b) in product(digits[:-1], signs)]
ls = [ls[i:i + len(signs)] for i in range(0, len(ls), len(signs))] + [[digits[-1]]]

pprint(func(200))
