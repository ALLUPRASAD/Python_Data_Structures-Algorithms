
from math import sqrt
def get_factors(n):
    results=[]
    def dfs(n,factor,path):
        for num in range(2,int(sqrt(n))+1):
            if n%num==0:
                divisor=n//num
                results.append(path+[divisor,num])
                dfs(divisor,num,path+[num])
    dfs(n,2,[])
    return results
get_factors(20)
