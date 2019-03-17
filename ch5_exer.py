#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import random


def ch5_exer_5_2(x, y):
    return x * y


def ch5_exer_5_3(x):
    x = int(x)
    print('input: %s' % x)
    if (x > 100) or (x < 0):
        print('input should between 0 and 100')
        return ''
    if (90 <= x <= 100):
        return 'A'
    elif (80 <= x < 90):
        return 'B'
    elif (70 <= x < 80):
        return 'C'
    elif (60 <= x < 70):
        return 'D'
    else:
        return 'F'


if __name__ == "__main__":
    print '%s * %s = %s' % (2, 3.0, ch5_exer_5_2(2, 3.0))
    for i in range(5):
        print(ch5_exer_5_3(random.randint(0, 100)))
