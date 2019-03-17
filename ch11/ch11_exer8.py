#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def is_leap_year(year):
    cond1 = (year % 4 == 0 and not year % 100 == 0)
    cond2 = (year % 400 == 0)
    if cond1 or cond2:
        return True
    else:
        return False


if __name__ == "__main__":
    years = [1992, 1996, 2000, 1967, 1900, 2400]
    for year in years:
        print is_leap_year(year),
    result = []
    for year in years:
        if is_leap_year(year):
            result.append(year)
    print result
    leap_years = [year for year in years if is_leap_year(year)]
    print filter(is_leap_year, years)
    print leap_years == filter(is_leap_year, years)
