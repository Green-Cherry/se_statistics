# -*- coding: utf-8 -*-
'''
一元线性回归
'''
import scipy.stats as sta
import math
import numpy as np
class Solution:
    def solve(self):
        X = [116.5, 120.8, 124.4, 125.5, 131.7, 136.2, 138.7, 140.2, 146.8, 149.6, 153.0, 158.2, 163.2, 170.5, 178.2,
             185.9]
        Y = [255.7, 263.3, 275.4, 278.3, 296.7, 309.3, 315.8, 318.8, 330.0, 340.2, 350.7, 367.3, 381.3, 406.5, 430.8,
             451.5]
        simple(Y,X,a=0.05)

def simple(data1,data2,a):
    n=len(data1)
    x_sum=sum(data1)
    y_sum=sum(data2)
    xy_sum=sum(data1[i]*data2[i] for i in range(len(data1)))
    x2_sum=sum(data1[i]*data1[i] for i in range(len(data1)))
    y2_sum=sum(data2[i]*data2[i] for i in range(len(data2)))

    lxy=xy_sum-(1.0*x_sum*y_sum)/n
    lxx=x2_sum-1.0*x_sum**2/n
    b_value=lxy/lxx
    a_value=avg(data2)-b_value*avg(data1)



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