# check even/odd
def check_even_odd(n):
    if (n & 1) == 1:
        return "odd"
    return "even"

# check decimal sight
def if_opposite_sign(x, y):
    if (x ^ y) < 0:
        return True
    return False

