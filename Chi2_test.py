#-*- coding:utf-8 -*-
'''
卡方参数检验
'''
# -*- coding: utf-8 -*-
import scipy.stats as sta
import math
class Solution:
    def solve(self):
        data=[1.26,1.13,0.98,1.12,1.23,0.99,1.98,1.11,1.70,1.17,
        1.19,0.96,1.10,1.12,0.74,1.45,1.97,1.54,2.37,1.12,
        1.31,1.06,1.12,0.95,1.50,1.24,0.91,1.08,1.38,1.23,
        0.97,1.00,1.03,1.02,0.50,1.01,1.22,1.10,1.60,0.82,
        1.81,0.94,1.16,1.13,0.59,2.03,1.06,1.64,1.26,0.86]
        chi_single_test([],0,0.01)

'''
单总体
服从正态分布
'''
def chi_single_test(data,sigma0,a):
    n=len(data)
    x_mean=avg(data)
    s=std(data,x_mean)
    chi=1.0*(n-1)*s**2/sigma0**2
    C=sta.chi2(n-1)
    chi_val=C.ppf(1-a)
    con=False if (chi>=chi_val) else True
    if(chi<0):
        p=C.cdf(chi)
    else:
        p=C.sf(chi)
    print(chi,p)
    return [round(chi,2),con]



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