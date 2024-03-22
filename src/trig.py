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
l:None
v:0.5
r:40
--NOTES--\n"""
    for item in arr:
        ret += str(round(item)) + ","
    ret = ret[:-1]
    ret += "\n--END--"
    return ret

def cos_cos():
    x = get_range(10, 0.1)
    y = [math.cos(math.cos(i))*1000 for i in x]
    return to_FMAP(y)

def sin_tan():
    x = get_range(10, 0.1)
    y = [math.sin(i)*math.tan(i)*1000 for i in x]
    return to_FMAP(y)

open("cos_cos.FMAP", "w").write(cos_cos())
open("sin_tan.FMAP", "w").write(sin_tan())