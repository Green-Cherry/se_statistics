# -*- coding: utf-8 -*-
import scipy.stats as sta
import math
class Solution:
    def solve(self):
        data1=[10,27,43,38,23,8,1,0]
        data2=[0,7,17,30,29,15,1,1]
        double_K_S(data1,data2)

def double_K_S(data1,data2):
    f_x = F_x(data1)
    g_x = F_x(data2)
    n1 = sum(data1)
    n2 = sum(data2)
    d = d_max(f_x, g_x)
    n = n1 * n2 / float(n1 + n2)
    print n

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
获取最大偏差
'''
def d_max(data1,data2):
    dif=[]
    for i in range(len(data1)):
        dif.append(math.fabs(data1[i] - data2[i]))
    d = max(dif)
    return d

s=Solution()
answer=s.solve()
print answer