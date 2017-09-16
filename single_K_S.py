# -*- coding: utf-8 -*-
import scipy.stats as sta
import math
class Solution:
    def solve(self):
        data1=[6,23,27,19,15,10]
        data2=[480,520,560,600,640,680]
        single_K_S_check(data1,data2)

def single_K_S_check(data1,data2):
    x_avg=577.6
    s=56.37
    f_x = F_x(data1)
    g_x = norm_value(data2,x_avg ,s )
    dif = d(f_x, g_x)
    n = sum(data1)
    print dif

'''
获取累计值F*(xi)
'''
def F_x(data):
    total=sum(data)
    f_x=[]
    x_data=data[:]
    f_x.append(data[0]/float(total))
    for i in range(1,len(data)):
        x_data[i]+=x_data[i-1]
        f_x.append(x_data[i]/float(total))
    return f_x

'''
获取正态分布的值
'''
def norm_value(data,x_avg,s):
    norm = sta.norm(x_avg, s)
    x=[]
    for i in range(len(data)):
        x.append(norm.cdf(data[i]))
    print x
    return x

'''
获取最大偏差
'''
def d(data1,data2):
    dif = []
    for i in range(len(data1)):
        dif.append(math.fabs(data1[i] - data2[i]))
    d = max(dif)
    return d

s=Solution()
answer=s.solve()
print answer