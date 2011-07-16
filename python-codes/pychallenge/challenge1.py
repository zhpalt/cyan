#! /usr/bin/env python
# coding=utf-8

abc = "abcdefghijklmnopqrstuvwxyz"

def translate(s):
    out = ""
    for c in s:
        if c <= 'z' and c >= 'a':
            a = abc.find(c) + 2
            a %= 26
            out += abc[a:a+1]
        else:
            out += c
    print(out)

if __name__ == "__main__":
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.0"
    translate(s)
