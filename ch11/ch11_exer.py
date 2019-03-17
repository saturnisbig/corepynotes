#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# 11-1
def countToFour1():
    for eachNum in range(5):
        print eachNum,

def countToFour2(n):
    for eachNum in range(n, 5):
        print eachNum,

def countToFour3(n=1):
    for eachNum in range(n, 5):
        print eachNum,

# 11-2
# input    countToFour1   countToFour2    countToFour3
# 2             E           2, 3, 4         2, 3, 4
# 4             E           4               4
# 5             E           None            None
# (nothing) 0,1,2,3,4       E               1, 2, 3, 4

def exer2():
    l = [2, 4, 5]
    funcs = {'1': countToFour1, '2': countToFour2, '3': countToFour3}
    for i in range(1, 4):
        for v in l:
            try:
                print 'Called: %s with args: %s' % (funcs[str(i)].func_name, v)
                funcs[str(i)](v)
                print
            except TypeError, e:
                print 'Error: %s ' % e

    for i in range(1, 4):
        try:
            print 'Called: %s with no args' % funcs[str(i)].func_name
            funcs[str(i)]()
            print
        except TypeError, e:
            print 'Error: %s ' % e

# 11-3
def max2(x, y):
    return x if x > y else y

def min2(x, y):
    return y if x > y else x

def my_max(seq=[]):
    """
    return max item of none empty sequence
    """
    result = None
    if seq:
        n = len(seq)
        if n > 0:
            result = seq[0]
            for i in range(n-1):
                result = max2(result, seq[i+1])
    return result

def my_min(seq=[]):
    """
    return min item of none empty sequence
    """
    result = None
    if seq:
        n = len(seq)
        if n > 0:
            result = seq[0]
            for i in range(n-1):
                result = min2(result, seq[i+1])
    return result


if __name__ == "__main__":
    # exer2()
    # print max2(4, 4)
    #print max2(4, 8)
    #print min2(4, 8)
    print my_max((1, 3, 5, 9))
    print my_max('abcd')
    print my_min((1, 3, 5, 9))
    print my_min('abcd')
