#! /usr/bin/env python
# coding=utf-8

l1 = [2, 3, 4, 5, 6, 7]

try:
    n = 2
    while n < 100:
        print "%d is on l1[%d]" % (n, l1.index(n))
        n += 1
except ValueError as e:
    print "[ERROR] %d is not in l1" % (n)
