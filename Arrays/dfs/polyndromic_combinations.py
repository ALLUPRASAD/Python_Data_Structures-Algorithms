#brute force approach 
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.results=[]
        p_results=[]
        def dfs(st,resul):
            if len(st)==0:
                if resul==resul[::-1]:
                    self.results.append(resul)
            for i in range(len(st)):
                ch=st[i]
                l=st[0:i]
                r=st[i+1:]
                res=l+r
                dfs(res,ch+resul)
        dfs(s,'')
        return set(self.results)
    
#2nd method with better time complexity
