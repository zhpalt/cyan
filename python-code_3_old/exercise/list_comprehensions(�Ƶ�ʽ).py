#! /usr/bin/env python
# coding=utf-8

a = [66.25, 333, 1, 34, 35, 22.34, 2]

b = [("%s * 2 = %s" % (x, x * 2)) for x in a]
for x in b:
    print(x, end='; ')
print('\n')

a = [x for x in a if x <= 34]
b = [(x, x ** 2) for x in a]
print(b, end='\n\n')

b = [x ** 2 for x in a]
c = [x + y for x in a for y in b]
print("for x in %s:\n    x + %s\n= %s\n" % (a, b, c))

c = [a[i] + b[i] for i in range(len(a))]
print("%s + %s = %s\n" % (a, b, c))
