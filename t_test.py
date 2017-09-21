# -*- coding: utf-8 -*-
import scipy.stats as sta
import math
class Solution:
    def solve(self):
        data = [159, 280, 101, 212, 224, 379, 179, 264,
                     222, 362, 168, 250, 149, 260, 485, 170]
        datax_iron = [78.1, 72.4, 76.2, 74.3, 77.4, 78.4, 76.0, 75.5, 76.7, 77.3]
        datay_iron = [79.1, 81.0, 77.3, 79.1, 80.0, 79.1, 79.1, 77.3, 80.2, 82.1]
        t_single_test(data,225,0.05)
        # t_double_test(datax_iron,datay_iron,0,0.05)
        # t_pair_test(datay_iron,datax_iron,0.05)

'''
单总体均值
服从正态分布
'''
def t_single_test(data,mu0,a):
    n=len(data)
    x_mean=avg(data)
    s=std(data,x_mean)
    t=(x_mean-mu0)*n**0.5/s
    T=sta.t(n-1)
    t_value=T.ppf(1-a)
    con=False if (t>=t_value) else True
    if(t<0):
        p=T.cdf(t)
    else:
        p=T.sf(t)
    print(t,p*2)
    # print sta.ttest_1samp(data,mu0)    #单样本均值检验，传入样本x和均值u，返回统计量和p值
    return [round(t,2),con]

'''
双总体均值差
服从正态分布，sigma1和2未知
'''
def t_double_test(data1,data2,delta,a):
    n1 = float(len(data1))
    n2 = float(len(data2))
    x_mean = sum(data1) / n1
    y_mean = sum(data2) / n2
    s1 = std(data1, x_mean)
    s2 = std(data2, y_mean)
    # (n1,n2,x_mean,y_mean,s1,s2)=(10,20,500,496,1.1,1.2)
    sw = (1.0 * ((n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2)) ** 0.5
    t=((x_mean-y_mean)-delta)/(sw*(1.0/n1+1.0/n2)**0.5)
    T = sta.t(n1 + n2 - 2)
    t_value = T.ppf(1 - a )
    con = False if (t >= t_value) else True
    if (t < 0):
        p = T.cdf(t)
    else:
        p = T.sf(t)
    print(t, p)
    return [round(t, 2), con]

'''
配对数据检验
'''
def t_pair_test(data1,data2,a):
    D=[]
    for i in range(len(data1)):
        D.append(data1[i]-data2[i])
    n=float(len(D))
    d_mean= sum(D) / n
    sd=std(D,d_mean)
    t=1.0*(d_mean*n**0.5)/sd

    T = sta.t(n - 1)
    t_value = T.ppf(1 - a)
    con = False if (t >= t_value) else True
    if (t < 0):
        p = T.cdf(t)
    else:
        p = T.sf(t)
    print(t, t_value)
    return [round(t, 2), con]


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