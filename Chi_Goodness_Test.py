#-*- coding:utf-8 -*-
'''
卡方拟合优度检验
'''
import scipy.stats as sta
import math
class Solution:
    def solve(self):
        result=[]
        data = [126, 131, 132, 132, 134, 135, 135, 136, 137, 137, 137, 137, 138, 138, 139,
                140, 140, 140, 140, 140, 140, 140, 141, 141, 141, 141, 141, 141, 142, 142
            , 142, 142, 142, 142, 142, 142, 143, 143, 143, 143, 143, 143, 144, 144, 144
            , 144, 144, 144, 145, 145, 145, 146, 146, 146, 146, 146, 146, 147, 147, 147
            , 147, 148, 148, 148, 148, 148, 149, 149, 149, 149, 149, 149, 150, 150, 150
            , 150, 152, 152, 153, 154, 154, 155, 158, 158]
        mu=avg(data)
        sigma=std(data,mu)
        result=chi_test(data,mu,sigma,a=0.05)
        return result

def chi_test(data,mu,sigma,a):
    n=len(data)
    #进行分组
    k=int(1+math.log(n)/math.log(2))
    distance=int(1.0*(max(data)-min(data))/k)+1
    group=[]
    frequency = []
    for i in range(k):
        group.append([min(data)+5*i-0.5,min(data)+5*i+4.5])
        frequency.append(0)

    for i in data:
        for j in range(k):
            if (i>=group[j][0] and i<group[j][1]):
                frequency[j]+=1

    while frequency[0]<5:
        frequency[0]+=frequency[1]
        frequency.remove(frequency[1])
        group[0][1]=group[1][1]
        group.remove(group[1])

    while frequency[len(frequency)-1]<5:
        frequency[len(frequency)-1]+=frequency[len(frequency)-2]
        frequency.remove(frequency[len(frequency)-2])
        group[len(group)-1][0]=group[len(group)-2][0]
        group.remove(group[len(group)-2])

    print mu,sigma,frequency,group

    #还没有计算概率值
    p=[]
    norm=sta.norm(mu,sigma)
    p.append(norm.cdf(group[0][1]))
    for i in range(1,len(group)-1):
        p.append(norm.cdf(group[i][1])-norm.cdf(group[i][0]))
    p.append(1-norm.cdf(group[len(group)-1][0]))
    print p

    #假设计算好了，计算卡方值
    chi=0
    for i in range(len(frequency)):
        chi+=1.0*frequency[i]**2/(n*p[i])
    chi-=n
    k=len(frequency)
    r=2
    dof=k-r-1
    C=sta.chi2(dof)
    con=False if chi>=C.ppf(1-a) else True
    print chi

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