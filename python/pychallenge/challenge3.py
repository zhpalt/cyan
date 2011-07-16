#! /usr/bin/env python
# coding=utf-8

def isbigletter(c):
    if ord(c) <= ord('Z') and ord(c) >= ord('A'):
        return True
    elif ord(c) <= ord('z') and ord(c) >= ord('a'):
        return False
    else:
        return None

s = open("data/challenge3.data").read();
out = ''
bigN1 = 0
bigN2 = 0
small = '0' #the small be surrounded
i = 0
for c in s:
    b = isbigletter(c)
    if b == True:
        if small != '0':
            bigN2 += 1
        else:
            bigN1 += 1
    elif b == False:
        if small != '0':
            if bigN1 == 3 and bigN2 == 3:
                out += small
                print(s[i - 7:i], ':', small)
            #reset
            bigN1 = bigN2
            bigN2 = 0
            small = c
        else:
            small = c
    i += 1

print("result:", out, "\n")

#other's best way
import re
print( "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', s)))
