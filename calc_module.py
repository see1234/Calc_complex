def c_sum(x, y):
    a = x[0]  # для красоты и понимания
    b = x[1]
    c = y[0]
    d = y[1]
    re = a + c
    im = b + d
    return [re, im]


def c_minus(x, y):
    a = x[0]  # для красоты и понимания
    b = x[1]
    c = y[0]
    d = y[1]
    re = a - c
    im = b - d
    return [re, im]


def c_mult(x, y):
    a = x[0]  # для красоты и понимания
    b = x[1]
    c = y[0]
    d = y[1]
    re = a * c - b * d
    im = b * c + a * d
    return [re, im]


def c_div(x, y):
    a = x[0]  # для красоты и понимания
    b = x[1]
    c = y[0]
    d = y[1]
    re = (a * c + b * d) / (c ** 2 + d ** 2)
    im = (b * c + a * d) / (c ** 2 + d ** 2)
    return [re, im]


def calc_complex(a, b, op):
    if op == "+":
        result = c_sum(a, b)
    elif op == "-":
        result = c_minus(a, b)
    elif op == "*":
        result = c_mult(a, b)
    elif op == "/":
        result = c_div(a, b)
    return result
