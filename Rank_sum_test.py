# -*- coding: utf-8 -*-
'''
秩和检验
'''
import scipy.stats as sta
import math
class Solution:
    def solve(self):
        # data1=[134,146,104,119,124,161,107,83,113,129,97,123]
        # data2=[70,118,101,85,112,132,94]
        data1=[2.36,3.14,7.52,3.48,2.76,5.43,6.54,7.41]
        data2=[4.38,4.25,6.54,3.28,7.21,6.54]
        a=0.05
        rank_sum_test(data1,data2,a)

'''
大样本的估计
'''
def rank_sum_test(data1,data2,a):
    data=data1+data2
    data=sorted(data)
    n1=len(data1)
    n2=len(data2)
    if (n1 < n2):
        t_data = data1
    else:
        t_data = data2
        n2 = len(data1)
        n1 = len(data2)
    T=0

    sign=[]
    #处理数字相同的情况，排序的序号要取平均,sign[]表示了每个数字对应的排序序号
    i=0
    while i <(len(data)-1):
        sum=i+1
        index=1
        while (data[i]==data[i+1]):
            sum+=i+2
            index+=1
            i+=1
        sum=sum/float(index)
        for j in range(index):sign.append(sum)
        i+=1
    if(data[len(data)-1]==data[len(data)-2]):
        sign.append(sign[len(sign)-1])
    else:sign.append(float(len(data)))
    print sign

    for i in range(len(data)):
        if(data[i] in t_data):
            t_data.remove(data[i])
            T+=sign[i]
    u=n1*(n1+n2+1)/2.0
    sigma=(n1*n2*(n1+n2+1)/12.0)**0.5
    U=math.fabs((T-u)/sigma)
    con=False if U>sta.norm.ppf(1-a/2) else True
    print con,T

s=Solution()
answer=s.solve()
print answer