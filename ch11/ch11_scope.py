#!/usr/bin/env python
# _*_ coding: utf-8 _*_

j, k = 1, 2

def proc1():
    j, k = 3, 4
    print "j == %d and k == %d" % (j, k)
    k = 5


def proc2():
    # j = 6
    global j
    proc1()
    print "j == %d and k == %d" % (j, k)


k = 7
# j == 3 and k == 4
proc1()
# j == 1 and k == 7
print "j == %d and k == %d" % (j, k)

j = 8
# j == 3 and k == 4
# j == 6 and k == 7
# if add global to j in proc2() then
# j == 8 and k == 7
proc2()
# j == 8 and k == 7
print "j == %d and k == %d" % (j, k)
