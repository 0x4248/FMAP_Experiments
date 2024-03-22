# FMAP Experiments
# A collection of experiments to test the FMAP audio file format.
# GitHub: https://www.github.com/lewisevans2007/FMAP_Experiments
# License: GNU General Public License v3.0
# By: Lewis Evans

import math
import matplotlib.pyplot


def get_range(end, step):
    ret = []
    total_num = end / step
    a = 0
    for i in range(int(total_num)):
        ret.append(a)
        a = a + step
    return ret


def to_FMAP(arr):
    ret = """t:None
d:None
l:Nonef
v:0.5
r:40
--NOTES--\n"""
    for item in arr:
        ret += str(round(item)) + ","
    ret = ret[:-1]
    ret += "\n--END--"
    return ret

def sqrt_x():
    x = get_range(100, 0.1)
    y = [math.sqrt(i)*100 for i in x]
    return to_FMAP(y)

def x_squared():
    x = get_range(10, 0.1)
    y = [i**2*1000 for i in x]
    return to_FMAP(y)

open("sqrt_x.FMAP", "w").write(sqrt_x())
open("x_squared.FMAP", "w").write(x_squared())