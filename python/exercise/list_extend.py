#! /usr/bin/env python
# coding=utf-8

l1 = [2, 3, 4, 5]
l2 = [6, 7, 8]
print(l1)
l1[len(l1):] = l2   # same as l1.extend(l2)
print(l1)