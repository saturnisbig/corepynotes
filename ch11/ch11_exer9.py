#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os

def average(l):
    total = reduce(lambda x, y: x+y, l)
    print total, len(l)
    return total / len(l)


def filter_cur_part_dir(path):
    """
    返回除当前目录和父目录外的文件
    """
    return filter(lambda x: x and x[0] != '.', os.listdir(path))


if __name__ == "__main__":
    print average(range(1, 13))
    print filter_cur_part_dir('/home/teddy/projects/toy/core-python')
