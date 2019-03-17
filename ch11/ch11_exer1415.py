#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def fib(n):
    # if n < 1:
    #     print 'Must greater than 1'
    #     return
    if n == 1 or n == 2:
        return 1
    x, y = 0, 1
    while n > 0:
        n = n - 1
        x, y = y, x+y
    print x
    return x

def fib2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

def forward(s):
    for c in s:
        print c

def bkwd(s):
    if len(s) == 1:
        print s
    else:
        print s[-1]
        return bkwd(s[:-1])


if __name__ == "__main__":
    # print fib(1) == fib2(1)
    # print fib(2) == fib2(2)
    # print fib(10) == fib2(10)
    bkwd('hello world!')
    forward('hello world!')
