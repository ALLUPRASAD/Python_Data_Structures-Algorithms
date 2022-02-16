class Solution(object):
    def subsets(self, nums):
        output=[]
        n=len(nums)
        for i in range(2**n,2**(n+1)):
            b=bin(i)[3:]
            output.append([nums[j] for j in range(n) if b[j]==str(1)])
        return output
