#!/usr/bin/env python
# _*_ coding: utf-8 _*_

'makeTextFile.py -- create text file'

import os

while True:
    fname = raw_input('输入文件名：')
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        break
    else:
        print('%s already exists. input another filename.')
    # if os.path.exists(fname):
    #     print('Error: "%s" already exists.' % fname)
    # else:
    #     break

all = []
print('\nEnter lines ("." by itself to quit).\n')

while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname, 'w')
fobj.write('\n'.join(all))
fobj.close()
print('DONE!')
