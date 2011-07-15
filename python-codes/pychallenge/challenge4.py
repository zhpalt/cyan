#! /usr/bin/env python
# coding=utf-8

import urllib.request

urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

i = 400
nothing = '65667'
while i > 0:
    url = urlbase + nothing
    data = urllib.request.urlopen(url)

    web = str(data.read())
    web = web[2:len(web) - 1]
    print web

    if web != 'Yes. Divide by two and keep going.':
        ss = web.split()
        nothing = ss[len(ss) - 1]
    else:
        nothing = str(int(nothing) // 2)
        print 'Divide by two:', nothing
