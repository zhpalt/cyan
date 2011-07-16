# coding=utf-8

s = open("data/challenge2.data").read()
out = ''
for c in s:
    if c >= 'a' and c <= 'z':
        out += c

print out