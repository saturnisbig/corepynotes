#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import time

class Date(object):
    fmt_dict = {
        'MDY': '%m/%d/%y',
        'MDYY': '%m/%d/%Y',
        'DMY': '%d/%m/%y',
        'DMYY': '%d/%m/%Y',
        'MODYY': '%a %d, %Y',
        'default': '%a %b %d %H:%M:%S %Y'
    }

    def __init__(self, t=time.time()):
        self.t = time.localtime(t)

    def update(self, t):
        if t:
            self.t = time.localtime(t)
        else:
            self.t = time.localtime()

    def display(self, fmt=''):
        f = Date.fmt_dict.get(fmt, '')
        if f:
            print time.strftime(f, self.t)
        else:
            f = '%a %b %d %H:%M:%S %Y'
            print time.strftime(f, self.t)


if __name__ == "__main__":
    d = Date()
    d.display('DMYY')
    d.display('MDYY')
    d.display('MODYY')
