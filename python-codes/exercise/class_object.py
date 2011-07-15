# coding=utf-8

class A:
    i = 1
    def __init__(self, num, status):
        self.status = status
        self.i = num
    def f(self, num):
        print '%d ** 2 = %d' % (num, num ** 2)
    @staticmethod
    def sf(num1, num2):
        print '%s / %s = %s' % (num1, num2, num1 / num2)
    def f2(self, num):
        num = num ** 2

x = A(24, 2)

# 成员测试
print 'x.i = %d' % x.i
print 'A.i = %d' % A.i
del x.status
x.status = 43
print 'x.status = %d' % x.status

# 函数测试
xf = x.f
xf(29)
af = A.f
af(x, 29)
asf = A.sf
asf(44, 6.0)
ii = 3
x.f2(ii)
print ii