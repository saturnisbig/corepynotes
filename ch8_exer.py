#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# 8-1


def exer81(x):
    """
    x < 0 : A, C
    x == 0: A, D
    x > 0 : A, B
    """
    # stmt A
    if x > 0:
        # stmt B
        pass
    elif x < 0:
        # stmt C
        pass
    else:
        # stmt D
        pass
        # stmt #

def exer82():
    print('请依次输入数字from, to, increment:')
    while True:
        f = int(raw_input('from:'))
        t = int(raw_input('to:'))
        inc = int(raw_input('increment:'))
        print '从%s到%s,每次递增%s' % (f, t, inc)
        print range(f, t+1, inc)
        cmd = raw_input('是否继续，y继续，n结束')
        if cmd.lower() == 'n':
            print 'Bye!'
            break

def exer83():
    """
    """
    print range(10)
    print range(3, 19, 3)
    print range(-20, 861, 220)


def is_prime(num):
    """
    exer8-4:给定一个数字，如果是素数则返回True，不是则False
    """
    if num == 1:
        return False
    mid = num / 2
    while mid > 1:
        if num % mid == 0:
            break
        mid -= 1
    else:
        # 2的话也会到这里来
        return True
    return False


def get_factors(num, itself=True):
    """
    exer8-5:接受一个数字，返回所有约数，包括1和它本身
    """
    result = []
    # 是否包含自身
    if itself:
        mid = num
    else:
        mid = num - 1
    while mid >= 1:
        if num % mid == 0:
            result.append(mid)
            # result.append(num/mid)
        mid -= 1
    return result


def get_prime_factors(num):
    """
    exer8-6:返回一个整数的所有素约数
    """
    result = []
    prime_factors = [i for i in get_factors(num) if is_prime(i)]
    while num > 1:
        for f in prime_factors:
            if num % f == 0:
                result.append(f)
                num = num / f
                break
    return result


def is_perfect(num):
    """
    exer8-7:完数--给定一个正数，如果约数的和与该整数相等，返回True，否则返回False
    """
    r = sum(get_factors(num, itself=False))
    if r == num:
        return True
    else:
        return False


def mult_n(num):
    """
    exer8-8:返回阶乘值
    """
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


def fib(n):
    """
    exer8-9:返回第n个fib数
    """
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    # exer82()
    # exer83()
    # print map(isprime, range(1, 20))
    # for i in range(1, 11):
    #     print get_factors(i)
    # print get_factors(90)
    # print get_prime_factors(20)
    # print is_perfect(6)
    # print mult_n(5)
    for i in range(1,11):
        print fib(i)
