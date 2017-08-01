# -*- coding: utf-8 -*-
'''
单因素方差分析
'''
import scipy.stats as sta
class Solution:
    def solve(self):
        data=[[25.6,22.2,28.0,29.8],[24.4,30.0,29.0,27.5],[25.0,27.7,23.0,32.2],[28.8,28.0,31.5,25.9],[20.6,21.2,22.0,21.2]]
        return  One_Way_Test(data)

def One_Way_Test(data):
    ST=get_ST(data)
    SA=get_SA(data)
    Se=ST-SA
    n=len(data)*len(data[0])
    m=len(data)
    fa=m-1
    fe=n-m
    Va=1.0*SA/fa
    Ve=1.0*Se/fe
    Fa=Va/Ve
    F=sta.f(fa,fe)
    F_5=F.ppf(0.95)
    F_1=F.ppf(0.99)
    print Fa, F_5, F_1
    if Fa>=F_1:
        return 2
    elif Fa<F_5 :
        return 0
    else:
        return 1


def get_ST(data):
    C = get_C(data)
    QT = get_QT(data)
    return QT-C

def get_SA(data):
    C = get_C(data)
    QA = get_QA(data)
    return QA - C

def get_C(data):
    n=len(data)*len(data[0])
    total1=[]
    for i in data:
        total1.append(sum(i))
    total2=sum(total1)
    return total2**2/float(n)

def get_QT(data):
    sum=0
    for i in data:
        for j in i:
            sum+=j**2
    return sum


def get_QA(data):
    total=0
    for i in data:
        total+=sum(i)**2
    return total/float(len(data[0]))

s=Solution()
answer=s.solve()
print answer