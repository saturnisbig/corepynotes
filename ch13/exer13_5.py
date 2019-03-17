#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import math

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)


class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # return '((%d, %d), (%d, %d))' % (self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        return '(%s, %s)' % (self.p1, self.p2)

    def length(self):
        return math.sqrt((self.p2.y-self.p1.y)**2+(self.p2.x-self.p1.x)**2)

    def slope(self):
        if self.p1.x == self.p2.x:
            return None
        else:
            return float(self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)


if __name__ == "__main__":
    p1 = Point(2, 4)
    p2 = Point(5, 8)
    print p1
    l = Line(p1, p2)
    print l, l.length(), l.slope()
