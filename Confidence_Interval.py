# -*- coding: utf-8 -*-
'''
置信区间
'''
import scipy.stats as sta
class Solution:
    def solve(self):
        print  double_mean_two([],[],0.05)

'''
单总体均值区间估计，sigma已知，mu未知
'''
def single_mean_one(data,sigma,a):
    n=float(len(data))
    mean=sum(data)/n
    upper=mean+sigma*sta.norm.ppf(1-a/2.0)/float(n**0.5)
    lower=mean-sigma*sta.norm.ppf(1-a/2.0)/float(n**0.5)
    return [lower,upper]

'''
单总体均值区间估计，sigma和mu未知
'''
def single_mean_two(data,a):
    n=float(len(data))
    t=sta.t(n-1)
    mean=sum(data)/n
    s=std(data,mean)
    upper=mean+s*t.ppf(1-a/2.0)/float(n**0.5)
    lower=mean-s*t.ppf(1-a/2.0)/float(n**0.5)
    return [lower,upper]

'''
单总体均值区间估计，不服从正态分布
'''
def single_mean_three(data,a):
    n=float(len(data))
    mean=sum(data)/n
    s=std(data,mean)
    upper=mean+s*sta.norm.ppf(1-a/2.0)/float(n**0.5)
    lower=mean-s*sta.norm.ppf(1-a/2.0)/float(n**0.5)
    return [lower,upper]

'''
单总体方差区间估计，sigma和mu未知
'''
def single_var(data,a):
    n = float(len(data))
    mean = sum(data) / n
    s=std(data,mean)
    chi = sta.chi2(n - 1)
    x1 = chi.ppf(1-a/2)
    x2 = chi.ppf(a/2)
    lower = 1.0*(n - 1) * s ** 2 / x1
    upper = 1.0*(n - 1) * s ** 2 / x2
    return [lower,upper]

'''
双总体均值差区间估计，u1和u2未知，sigma1和sigma2已知
'''
def double_mean_one(data1,data2,sigma1,sigma2,a):
    n1 = float(len(data1))
    n2 = float(len(data2))
    x_mean = sum(data1) / n1
    y_mean = sum(data2) / n2
    s1=sigma1
    s2=sigma2
    z = sta.norm.ppf(1-a/2.0)
    lower = x_mean-y_mean-z*(1.0*s1**2/n1+1.0*s2**2/n2)**0.5
    upper = x_mean-y_mean+z*(1.0*s1**2/n1+1.0*s2**2/n2)**0.5
    return [lower,upper]

'''
双总体均值差区间估计，u1和u2，sigma1和sigma2未知，小样本
'''
def double_mean_two(data1,data2,a):
    n1 = float(len(data1))
    n2 = float(len(data2))
    x_mean = sum(data1) / n1
    y_mean = sum(data2) / n2
    s1=std(data1,x_mean)
    s2=std(data2, y_mean)
    # (n1,n2,x_mean,y_mean,s1,s2)=(10,20,500,496,1.1,1.2)
    sw=(1.0*((n1-1)*s1**2+(n2-1)*s2**2)/(n1+n2-2))**0.5
    print sw
    T = sta.t(n1+n2 - 2)
    t=T.ppf(1-a/2.0)
    lower = x_mean-y_mean-t*sw*(1.0/n1+1.0/n2)**0.5
    upper = x_mean-y_mean+t*sw*(1.0/n1+1.0/n2)**0.5
    return [lower,upper]

'''
双总体均值差区间估计，不服从正态分布，大样本
'''
def double_mean_three(data1,data2,a):
    n1 = float(len(data1))
    n2 = float(len(data2))
    x_mean = sum(data1) / n1
    y_mean = sum(data2) / n2
    s1=std(data1,x_mean)
    s2=std(data2, y_mean)
    z = sta.norm.ppf(1-a/2.0)
    lower = x_mean-y_mean-z*(1.0*s1**2/n1+1.0*s2**2/n2)**0.5
    upper = x_mean-y_mean+z*(1.0*s1**2/n1+1.0*s2**2/n2)**0.5
    return [lower,upper]

'''
双总体方差比区间估计，正态分布，u1和u2，sigma1和sigma2未知
'''
def double_var(data1,data2,a):
    n1 = float(len(data1))
    n2 = float(len(data2))
    x_mean = sum(data1) / n1
    y_mean = sum(data2) / n2
    s1=std(data1,x_mean)
    s2=std(data2, y_mean)
    F=sta.f(n1-1,n2-1)
    f1=F.ppf(1-a/2.0)
    f2=F.ppf(a/2.0)
    lower = s1**2/(s2**2*f1)
    upper = s1**2/(s2**2*f2)
    return [lower,upper]

'''
二项分布区间估计
'''
def binom_area(data,alpha):
    n = float(len(data))
    x_mean = sum(data) / n
    z=sta.norm.ppf(1-alpha/2.0)
    a=n+z**2
    b=-(2*n*x_mean+z**2)
    c=n*x_mean**2
    lower = (-b-(b**2-4*a*c)**0.5)/(2.0*a)
    upper = (-b+(b**2-4*a*c)**0.5)/(2.0*a)
    return [lower,upper]


def std(data,mean):
    sum=0
    for i in range(len(data)):
        sum+=(data[i]-mean)**2
    return (sum*1.0/(len(data)-1))**0.5

# s=Solution()
# answer=s.solve()
# print answer
print  binom_area([],0.05)