def r_div(x, y):
    return x / y

def r_mult(x, y):
    return x * y

def r_minus(x, y):
    return x - y

def r_sum(x, y):
    return x + y

def operation(op, x, y): 
    if op == "+":
        return r_sum(x, y)
    elif op == "-":
        return r_minus(x, y)
    elif op == "*":
        return r_mult(x, y)
    elif op == "/":
        return r_div(x, y)