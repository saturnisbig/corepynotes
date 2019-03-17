#!/usr/bin/env python
# _*_ coding: utf-8 _*_

'readTextFile.py -- read and display text file'

import os

fname = raw_input('Enter filename: ')
print

if os.path.exists(fname):
    fobj = open(fname, 'r')
    for line in fobj:
        print line.strip('\n')
    fobj.close()
else:
    print('*** file does not exists ***')

# try...except
# try:
#     fobj = open(fname, 'r')
# except IOError, e:
#     print('*** file open error ***', e)
# else:
#     for line in fobj:
#         print(line)
#    fobj.close()
