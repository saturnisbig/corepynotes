#!/usr/bin/env python
# _*_ coding: utf-8 _*_

class RoundFloat(float):
    '''Inherit immutable type float.'''
    def __new__(cls, val):
        return float.__new__(cls, round(val, 2))

class SortedKeyDict(dict):
    '''Inherit from mutable type.'''
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())
        # 下述方法会引起递归调用溢出
        # return sorted(self.keys())


class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj
    def get(self):
        return self.__data
    def __repr__(self):
        return repr(self.__data)
    def __str__(self):
        return str(self.__data)
    def __getattr__(self, attr):
        return getattr(self.__data, attr)


class HideX(object):
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return ~self.__x

    def set_x(self, x):
        assert isinstance(x, int), '"x" must be integer!'
        self.__x = ~x

    x = property(get_x, set_x)

# p609
class ProtectAndHideX(object):
    def __init__(self, x):
        self.x = x

    def x():
        def fget(self):
            return ~self.__x
        def fset(self, x):
            assert isinstance(x, int), \
                '"x must be an integer."'
            self.__x = ~x
        return locals()

    x = property(**x())

# p550
class P(object):
    def __init__(self):
        print "calling P's constructor"

class C(P):
    def __init__(self):
        super(C, self).__init__()
        print "calling C's constructor"


if __name__ == "__main__":
    c = C()
    inst2 = HideX(20)
    print inst2.x
    inst2.x = 30
    print inst2.x
    inst = ProtectAndHideX(40)
    # inst.x = 40
    print inst.x
    print dir(inst)
    # print RoundFloat(1.5955)
    # print RoundFloat(1.5945)
    # print RoundFloat(-1.9955)
    # d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2)))
    # print 'By iterator:'.ljust(12), [key for key in d]
    # print 'By keys():'.ljust(12), d.keys()
    wrappedList = WrapMe([123, 'foo', 45.67])
    wrappedList.append('bar')
    wrappedList.append(123)
    print wrappedList
    print wrappedList.pop()
    realList = wrappedList.get()
    print realList[3]
    # print wrappedList[3]
