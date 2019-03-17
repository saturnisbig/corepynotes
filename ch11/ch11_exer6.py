#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def printf(fmt='', *args):
    print fmt % args


if __name__ == "__main__":
    fmt = '%d %s %d'
    printf(fmt, 1, 'abc', 2)
