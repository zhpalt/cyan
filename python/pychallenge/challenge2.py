#! /usr/bin/env python
# coding=utf-8

s = open("data/challenge2.data").read()
out = ''
for c in s:
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        out += c

print(out)

