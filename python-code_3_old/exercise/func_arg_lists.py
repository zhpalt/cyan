#! /usr/bin/env python
# coding=utf-8

def f(x, *args, **keys):
    '''Function argument lists test

    f(x, a, b, c..., key1=e, key2=f...)
    '''
    print x
    for arg in args:
        print arg, '; '
    print '\n'
    ks = keys.keys()
    for key in ks:
        print key, ':', keys[key], '; '
    print '\n'

f(1, 45, 32, 23, 'aa', 'bb', key1='rtd', set=34)
