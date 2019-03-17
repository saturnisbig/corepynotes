#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import time


def timeit(func, *args, **kwargs):
    print 'Run func: ', func.__name__, args, kwargs
    start = time.time()
    r = func(*args, **kwargs)
    cost = time.time() - start
    print 'the return value is: ', r
    print 'the time elapsed: ', cost
    return (r, cost)

def test_func(tm, n=100):
    time.sleep(tm)
    r = 0
    for i in range(n):
        r += i
    return r

if __name__ == "__main__":
    timeit(range, 1, 100)
    timeit(test_func, 5)
