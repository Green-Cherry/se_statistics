# -*- coding: utf-8 -*-
'''
偏度峰度检验
'''
import scipy.stats as sta
import math
class Solution:
    def solve(self):
        data=[126,131,132,132,134,135,135,136,137,137,137,137,138,138,139,
140 ,140 ,140, 140 ,140, 140 ,140, 141 ,141, 141, 141, 141, 141, 142,142
,142, 142, 142, 142, 142 ,142 ,143, 143 ,143 ,143, 143, 143, 144, 144 ,144
,144, 144, 144, 145, 145 ,145 ,146, 146, 146 ,146, 146, 146, 147, 147, 147
,147, 148, 148, 148, 148 ,148 ,149, 149 ,149 ,149, 149, 149, 150, 150, 150
,150, 152, 152, 153, 154 ,154, 155, 158 ,158]
        a=0.1
        skew_kurt_check(data,a)


def skew_kurt_check(data,a):
    data_avg=avg(data)
    n=len(data)
    # print n
    s=std(data,data_avg)
    # g1=1.0*Bk(data,data_avg,3)/Bk(data,data_avg,2)**1.5
    # g2=1.0*Bk(data,data_avg,4)/Bk(data,data_avg,2)**2
    # print Bk(data,data_avg,3),Bk(data,data_avg,4)
    A1,A2,A3,A4=Ak(data,1),Ak(data,2),Ak(data,3),Ak(data,4)
    # print A1,A2,A3,A4
    B2=A2-A1**2
    B3=A3-3*A2*A1+2*A1**3
    B4=A4-4*A3*A1+6*A2*A1**2-3*A1**4
    g1=1.0*B3/B2**1.5
    g2=1.0*B4/B2**2
    sigma1=(1.0*6*(n-2)/((n+1)*(n+3)))**0.5
    sigma2=(1.0*24*n*(n-2)*(n-3)/((n+1)**2*(n+3)*(n+5)))**0.5
    u=3-6/float(n+1)
    u1=math.fabs(g1/sigma1)
    u2=math.fabs((g2-u)/sigma2)
    con=False if u1>=sta.norm.ppf(1-1.0*a/4) or u2>=sta.norm.ppf(1-1.0*a/4) else True
    print con

def avg(data):
    s=sum(data)
    return 1.0*s/len(data)

def std(data,x_avg):
    sum=0
    for i in range(len(data)):
        sum+=(data[i]-x_avg)**2
    return (sum*1.0/(len(data)-1))**0.5

def Ak(data,k):
    n=len(data)
    sum=0
    for i in data:
        sum+=i**k
    return sum/float(n)

def Bk(data,avg,k):
    n=len(data)
    sum=0
    for i in data:
        sum+=(i-avg)**k
    return sum/float(n)

s=Solution()
answer=s.solve()
print answer