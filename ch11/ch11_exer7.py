#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def merge_list(l1, l2):
    n = len(l1)
    result = []
    for i in range(n):
        result.append((l1[i], l2[i]))
    return result


def merge_list2(l1, l2):
    return zip(l1, l2)


if __name__ == "__main__":
    l1 = [i for i in range(1, 6)]
    l2 = ['abc', 'def', 'ghi', 'jkl', 'nmo']
    print merge_list(l1, l2)
    print merge_list2(l1, l2)

