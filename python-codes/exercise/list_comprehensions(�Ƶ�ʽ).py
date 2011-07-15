#! /usr/bin/env python
# coding=utf-8

a = [66.25, 333, 1, 34, 35, 22.34, 2]

b = [("%s * 2 = %s" % (x, x * 2)) for x in a]
for x in b:
    print x, '; ',
print '\n'

a = [x for x in a if x <= 34]
b = [(x, x ** 2) for x in a]
print b, '\n'

b = [x ** 2 for x in a]
c = [x + y for x in a for y in b]
for i in range(len(a)):
    for j in range(len(b)):
        print a[i], '+', b[j], '=', c[i * len(a) + j]
print

c = [a[i] + b[i] for i in range(len(a))]
for i in range(len(a)):
    print a[i], '+', b[i], '=', c[i]