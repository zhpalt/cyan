#! /usr/bin/env python
# coding=gbk

import math
import pdb

def fermat_factoring(n):
    """ Fermat's factoring """
    x = int(math.sqrt(n)) + 1
    y = x * x - n
    q = math.sqrt(y)

    while q > int(q) or q * q != y:   # ���q�Ƿ�Ϊƽ����
        x += 1
        if x >= n:      # �߽���
            return None
        y = x * x - n
        q = math.sqrt(y)

        # �������(debug only)
        if x % 1000000 == 0:
            print(x)

    y = int(q)
    if x == q or x + q >= n:    # ��Ч���ж�
        return None
    else:
        return x, y

def main():
    n = 368933789477
    it = fermat_factoring(n)
    if it == None:
        print(n, 'is a prime number')
    else:
        x, y = it
        print('x:', x, '; ', 'y:', y)
    
        if x < y:
            x, y = y, x
    
        x, y = x + y, x - y
        if x * y % n != 0:
            print('Error')
        else:
            q = x * y / n
            if q > 1:
                if x % q == 0:
                    x //= q
                else:
                    y //= q
            print(n, '=', x, '*', y)
            
if __name__ == '__main__':
    main()
