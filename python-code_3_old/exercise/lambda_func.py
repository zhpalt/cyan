def make_plus_func(n):
    return lambda x: x + n

def make_sqrt_func(n):
    return lambda x: pow(x, 1/n)

f_plus_3 = make_plus_func(3)
f_sqrt_3 = make_sqrt_func(3)
print f_plus_3(10)
print f_sqrt_3(10)
