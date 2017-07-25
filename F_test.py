# -*- coding: utf-8 -*-
import scipy.stats as sta
import math
class Solution:
    def solve(self):
        data = [159, 280, 101, 212, 224, 379, 179, 264,
                     222, 362, 168, 250, 149, 260, 485, 170]
        datax_iron = [78.1, 72.4, 76.2, 74.3, 77.4, 78.4, 76.0, 75.5, 76.7, 77.3]
        datay_iron = [79.1, 81.0, 77.3, 79.1, 80.0, 79.1, 79.1, 77.3, 80.2, 82.1]
        f_double_test(datax_iron,datay_iron,0.05)

'''
双总体均值差
服从正态分布，sigma1和2未知
'''
def f_double_test(data1,data2,a):
    n1 = float(len(data1))
    n2 = float(len(data2))
    x_mean = sum(data1) / n1
    y_mean = sum(data2) / n2
    s1 = std(data1, x_mean)
    s2 = std(data2, y_mean)
    f=1.0*s1**2/s2**2
    F = sta.f(n1-1, n2-1)
    f_value = F.ppf(1- a)
    con = False if (f >= f_value) else True
    if (f < 0):
        p = F.cdf(f)
    else:
        p = F.sf(f)
    print(f,f_value)
    return [round(f, 2), f_value]


def avg(data):
    s=sum(data)
    return 1.0*s/len(data)

def std(data,x):
    sum=0
    for i in range(len(data)):
        sum+=(data[i]-x)**2
    return (sum*1.0/(len(data)-1))**0.5


s=Solution()
answer=s.solve()
print answer