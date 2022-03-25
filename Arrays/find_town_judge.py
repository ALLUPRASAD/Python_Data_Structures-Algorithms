class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n==1:
            return 1
        d1={}
        d2={}
        for i,j in trust:
            if i in d2:
                d2[i]=d2[i]+1
            else:
                d2[i]=1
            if j in d1:
                d1[j]=d1[j]+1
            else:
                d1[j]=1

        for x,y in d1.items():
            if y==n-1:
                if x not in d2:
                    return x
        return -1
