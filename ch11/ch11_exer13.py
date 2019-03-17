#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from ch11_exer12 import timeit

def mult(x, y):
    return x * y

def fac1(n):
    # return reduce(mult, range(1, n+1))
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x *y, range(1, n+1))

def fac2(n):
    if n == 0 or n == 1:
        return 1
    return n * fac2(n-1)

def fac3(n):
    r = n
    if r == 0 or r == 1:
        return 1
    else:
        while n > 1:
            n = n - 1
            r = r * n
    return r


if __name__ == "__main__":
    print fac1(10)
    print fac2(100)
    print fac3(1000)
    # timeit(fac1, 1000)
    # timeit(fac2, 1000)
    # timeit(fac3, 1000)
