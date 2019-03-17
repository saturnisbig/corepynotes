#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# Create a class to format floating point values to monetary amounts.

def dollarize(f, sign='-'):
    '''
    takes a floating point value and returns that value as a
    string properly formatted with symbols and rounded to obtain
    a financial amount. Any negative sign should appear to the left of the
    dollar sign. For example:
        dollarize(1234567.8901) => '$1,234,567.89'
        dollarize(-1234567.8901) => '-$1,234,567.89'
    '''
    # fs = '%.2f' % f
    flag = 0
    if f < 0:
        f = -f
        flag = 1
    fs = '$' + format(f, '0,.2f')
    return sign + fs if flag else fs


class MoneyFmt(object):
    def __init__(self, value=0.0):
        self.value = float(value)

    def update(self, value=None):
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        val = dollarize(self.value)
        return val

    def __nonzero__(self):
        '''return bool or int if value is not zero'''
        # return self.value
        return self.value != 0


if __name__ == "__main__":
    print dollarize(1234567.8901)
    print dollarize(-1234567.8901)
    cash = MoneyFmt(123.45)
    print cash
    cash.update(10000.4567)
    print cash
    print repr(cash)
    cash.update(-0.3)
    print cash
    # print str(cash)
    if cash:
        print cash


