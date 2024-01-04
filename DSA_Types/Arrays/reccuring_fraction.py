class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        s=""
        t={}
        rem=numerator%denominator
        while rem!=0 and rem not in t:
            t[rem]=len(s)
            rem=rem*10
            resul=rem//denominator
            s=s+str(resul)
            rem=rem%denominator
        if rem==0:
            return ''
        else:
            return s[t[rem]:]
            
        
