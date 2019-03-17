#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os


def exer91(fname):
    """
    显示一个文件的所有行，忽略以#开头的行，Python等语言的注释；
    处理不是第一个字符开头的注释
    """
    fobj = open(fname, 'r')
    result = []
    for line in fobj:
        line = line.strip()
        if line.startswith('#'):
            continue
        else:
            index = line.find('# ')
            if index != -1:
                line = line[:index]
                result.append(line.strip())
            else:
                result.append(line)
    fobj.close()
    return result


def comment_char(c):
    pass


def exer92():
    """
    提示输入数字N和文件F，然后显示文件F的前N行。
    """
    ln = int(raw_input("请输入读取行数："))
    fname = raw_input("请输入文件名：")
    for i, line in enumerate(open(fname, "rU")):
        if i < (ln -1):
            print line
        else:
            break


def exer93(fname=""):
    """
    提示输入一个文件名，显示总行数
    """
    if not fname:
        fname = raw_input("请输入文件名：")
    fh = open(fname, 'r')
    # read all lines into a list
    count = len(fh.readlines())
    # use iterator to count for big file
    fh.seek(0)
    count1 = -1
    for count1, line in enumerate(fh):
        pass
    count1 += 1
    print count, count1


def exer94(page_num=25):
    test_f = open('exer94.txt', 'w')
    for i in range(100):
        test_f.write(str(i+1) + '\n')
    test_f.close()
    # fname = raw_input("请输入文件名：")
    fname = 'exer94.txt'
    for i, line in enumerate(open(fname, 'rU')):
        print line
        if (i+1) % page_num == 0:
            press_any_key_continue("按任意键继续")
            # os.system("read -s -n 1 -p '按任意键继续'")
            # print
            # continue
            # raw_input("按任意键继续。")


def press_any_key_continue(prompt):
    import termios, sys
    # 获取标准输入符
    fd = sys.stdin.fileno()
    # 获取标准输入（终端）设置
    old_ttyinfo = termios.tcgetattr(fd)
    # 配置终端
    new_ttyinfo = old_ttyinfo[:]
    new_ttyinfo[3] = new_ttyinfo[3] & ~termios.ICANON
    new_ttyinfo[3] &= ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
    os.read(fd, 7)
    termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)


def exer96():
    """
    比较两个文本程序，如果不同，给出第一个不同处的行号和列号
    """
    f1 = open(raw_input("请输入第一个文件名："), 'r')
    f2 = open(raw_input("请输入第二个文件名："), 'r')
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    ln = max(len(lines1), len(lines2))
    f1.close()
    f2.close()
    i = 0
    while ln > i:
        cols = max(len(lines1[i]), len(lines2[i]))
        for j in range(cols):
            # print lines1[i][j],
            try:
                if lines1[i][j] != lines2[i][j]:
                    print "有区别的行:%d, 列：%d" % (i+1, j+1)
                    return i+1, j+1
            except IndexError:
                print "有区别的行:%d, 列：%d" % (i+1, j+1)
                return i+1, j+1
        i += 1
    print "两个文件内容一样"


def exer97(fname='/etc/services'):
    fd = open(fname, 'r')



if __name__ == "__main__":
    print exer91('/etc/services')
    # exer92()
    # exer93()
    # exer94()
    # exer96()
