class Solution(object):
    def longestPalindrome(self, s):

        x=[]
        for i in range(len(s)):
            for j in range(1,len(s)+1):
                if s[i:j]!='' and s[i:j]==s[i:j][::-1] :
                    x.append(s[i:j])
        if x:
            return max(x,key=len)
        else:
            return s
