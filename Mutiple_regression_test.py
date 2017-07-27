# -*- coding: utf-8 -*-
'''
多元线性回归
'''
import scipy.stats as sta
import math
import numpy as np
class Solution:
    def solve(self):
        y = [162, 120, 223, 131, 67, 169, 81, 192, 116, 55, 252, 232, 144, 103, 212]

        x1=[274, 180, 375, 205, 86, 265, 98, 330, 195, 53, 430, 372, 236, 157, 370]
        x2=[2450, 3250, 3802, 2838, 2347, 3782, 3008, 2450, 2137, 2560, 4020, 4427, 2660, 2088, 2605]
        x0=[]
        for i in range(len(x1)):x0.append(1)
        x=[x0,x1,x2]
        multiple(x,y,a=0.05)

def multiple(x,y,a):
    y=np.mat(y).T
    x=np.mat(x).T
    beta=(x.T*x).I*x.T*y
    print beta

    def mutiple_regression_test(self, datay, datax_2d, a):
        """
        :param datax_2d: 样本X
        :param datay: 样本Y
        :param a:     置信水平
        :return:      [拟合系数 ,F统计量 ， 显著性]
        """

        eyey = []

        n = len(datay)
        for i in range(len(datay)):
            eyey.append(1)
        datax = datax_2d
        datax.insert(0, eyey)

        matX = np.mat(datax)
        matX = matX.transpose()
        matY = np.mat(datay)
        matY = matY.transpose()

        one = np.ones(n)
        matOne = np.mat(one)
        J = matOne.T * matOne
        beta = (matX.T * matX).I * matX.T * matY
        H = matX * (matX.T * matX).I * matX.T
        I = np.eye(n)
        e = (I - H) * matY
        ST = matY.T * matY - (matY.T * J * matY) / float(n)
        Se = matY.T * matY - beta.T * matX.T * matY
        SR = ST - Se
        r2 = SR / ST
        m = len(beta)
        VR = SR / float(m - 1)
        Ve = Se / float(n - m)

        print SR, Se
        value = float(VR) / float(Ve)

        fA = m - 1
        fe = n - m

        fa1 = f.ppf(0.95, fA, fe)
        fa2 = f.ppf(0.99, fA, fe)
        result = ''
        if value > fa1 and value < fa2:
            result = '*'
        if value > fa2:
            result = '**'

        print value
        return [beta, float(value), result]

s=Solution()
answer=s.solve()
print answer
