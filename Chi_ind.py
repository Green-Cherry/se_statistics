#-*- coding:utf-8 -*-
'''
卡方独立检验
'''
import scipy.stats as sta
class Solution:
    def solve(self):
        result=[]
        data=[[186,38,35],[227,54,45],[219,78,78],[355,112,140],[653,285,259]]
        result=chi_ind(data)
        return result

def chi_ind(data):
    row=len(data)
    col=len(data[0])
    xi=[]
    yi=[]
    for i in data:
        xi.append(sum(i))

    for j in range(col):
        y_sum=0
        for i in range(row):
            y_sum+=data[i][j]
        yi.append(y_sum)

    total=sum(xi)
    chi_val=0
    for i in range(row):
        for j in range(col):
            tij=xi[i]*yi[j]/float(total)
            chi_val+=1.0*(data[i][j]-tij)**2/tij

    dof=(row-1)*(col-1)
    chi=sta.chi2(dof)
    return [round(dof,2),round(chi_val,2),chi_val<chi.ppf(0.99)]

s=Solution()
answer=s.solve()
print answer