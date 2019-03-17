#!/usr/bin/env python
# _*_ coding: utf-8 _*_

print(1 + 2*4)


# 2-4
def ch2_exer_2_4():
    """打印用户的输入值."""
    s = raw_input('请输入字符串：')
    print(s)
    i = raw_input('请输入数值：')
    print(int(i))


# 2-5
def ch2_exer_2_5():
    """使用while和for分别输出0-10."""
    print("使用while输出：\n")
    x = 0
    while x <= 10:
        print x,
        x += 1
    # 打印空格
    print
    print("使用range输出：\n")
    for i in range(11):
        print i,


# 2-6
def ch2_exer_2_6():
    """判断正数、负数、0"""
    i = int(raw_input('请输入一个整数：'))
    print('输入的是：%s\n' % i)
    if i < 0:
        print('负数')
    elif i == 0:
        print('0')
    else:
        print('正数')


# 2-7
def ch2_exer_2_7():
    """用户输入一个字符串，逐个字符打印出来，分别用while和for实现"""
    s = raw_input('请输入一个字符串：')
    print('先用while实现：')
    i = 0
    while i < len(s):
        print s[i] + ' ',
        i += 1
    print
    print('用for实现：')
    for i in range(len(s)):
        print s[i] + ' ',


def ch2_exer_2_8():
    l = [2, 3, 4, 5, 9]
    print('先用while实现：')
    llen = len(l)
    r1 = 0
    while llen > 0:
        r1 += l[llen-1]
        llen -= 1
    print '结果：', r1

    print('用for实现：')
    r2 = 0
    for i in range(len(l)):
        r2 += l[i]
    print '结果：', r2
    print('用户输入数值：')
    r3 = 0
    for i in range(5):
        x = int(raw_input('请输入数值：'))
        r3 += x
    print '结果：', r3


def ch2_exer_2_9(n=5):
    r = 0
    i = 0
    while i < n:
        a = int(raw_input('请输入数值：'))
        r += a
        i += 1
    print('结果为：')
    print float(r) / n


def ch2_exer_2_10():
    while True:
        i = int(raw_input('请输入一个1到100间的数：'))
        if i < 1:
            print('输入的数小于1')
        elif i > 100:
            print('输入的数大于100')
        else:
            print('You done!')
            break


def ch2_exer_2_11():
    """文本菜单，用户选择功能"""
    menu = """
    (1)求5个数的和；
    (2)求5个数的平均值；
    (X)退出
    请选择：
    """
    while True:
        choice = raw_input(menu)
        if choice == '1':
            ch2_exer_2_8()
        elif choice == '2':
            ch2_exer_2_9()
        elif choice.lower() == 'x':
            print('退出')
            break
        else:
            continue


if __name__ == "__main__":
    ch2_exer_2_11()
