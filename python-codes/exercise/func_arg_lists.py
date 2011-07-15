#! /usr/bin/env python
# coding=gbk

def f(x, *args, **keys):
    '''Function argument lists test

    f(x, a, b, c..., key1=e, key2=f...)
    '''
    import pdb
    print x
    for arg in args:
        print '%s; ' % arg,
    print
    ks = keys.keys()
    for key in ks:
        print '%s:%s; ' % (key, keys[key]),
    print

f(1, 45, 32, 23, 'aa', 'bb', key1='rtd', set=34)
