# -*- coding: utf-8 -*-
import scipy.stats as sta
import math
'''
符号检验
'''
class Solution:
    def solve(self):
        data=[7800,7400,7300,6700,7000,7800,8200,7400,8300,6800,7700,7700,7400,12900,7500,7700]
        sign_single_test(data,7900,0.05)


'''
单总体分位数检验
'''
def sign_single_test(data,mu0,a):
    n=len(data)
    n_posi=0
    for i in data:
        if i>mu0:
            n_posi+=1
    B=sta.binom(n,0.5)
    p=B.cdf(n_posi)
    con = False if (p<a/2.0) else True
    print p,con


'''
双总体符号检验
根据p值判断
'''
def sign_double_test_one(data1,data2,a):
    n_posi=0
    n=len(data1)
    for i in range(n):
        if(data1>data2):
            n_posi+=1
    # (n_posi,n)=(30,40)
    B = sta.binom(n, 0.5)
    p = B.sf(n_posi-1)
    con = False if (p < a / 2.0) else True
    print p,con

'''
双总体符号检验
根据临界值判断
'''
def sign_double_test_two(data1,data2,a):
    n_posi=0
    n=len(data1)
    for i in range(n):
        if(data1>data2):
            n_posi+=1
    # (n_posi,n)=(30,40)
    B = sta.binom(n, 0.5)
    c1=B.ppf(a/2.0)
    c2=B.ppf(1-a/2.0)
    if (B.cdf(c1)>a/2.0):
        c1=c1-1
        c2=c2+1

    con = False if (n_posi<=c1 or n_posi>=c2) else True
    print c1,c2,con


s=Solution()
answer=s.solve()
print answer