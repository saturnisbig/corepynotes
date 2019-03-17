#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2


def doprob():
    'help doc here'
    op = choice('+-')


from time import ctime, sleep


def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc


@tsfunc
def foo():
    pass

def tsmain():
    foo()
    sleep(4)
    for i in range(2):
        sleep(1)
        foo()

def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1

if __name__ == "__main__":
    tsmain()
