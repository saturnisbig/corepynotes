#!/usr/bin/env python
# _*_ coding: utf-8 _*_


# 3-12 合并文件，让用户选择是创建还还是读取文件
# 有难度
# 3-13 添加允许用户编辑输入的功能，可以按行也可以整篇修改？

import os


def write_text_file():
    while True:
        fname = raw_input('请输入要创建的文件名：')
        if os.path.exists(fname):
            print('Error: %s 文件已经存在!' % fname)
        else:
            break
    all = []
    while True:
        entry = raw_input('请输入内容，以"."结束输入> ')
        if entry == '.':
            break
        else:
            all.append(entry)
    fobj = open(fname, 'w')
    fobj.write('\n'.join(all))
    fobj.close()


def read_text_file():
    fname = raw_input('请输入文件名：')
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print('*** open file error ***')
    else:
        print('-------文件内容开始---------')
        for line in fobj:
            print line.strip()
        print('-------文件内容结束---------\n')
        fobj.close()


def main():
    while True:
        choice = raw_input('1. 写入文件；\n2. 读取文件；\nX退出!\n')
        choice = choice.lower()
        if choice == '1':
            write_text_file()
        elif choice == '2':
            read_text_file()
        elif choice == 'x':
            break
        else:
            print('请输入正确的选择!')


if __name__ == "__main__":
    main()
