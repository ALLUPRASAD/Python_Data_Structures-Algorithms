class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in nums:
            c=0
            for j in nums:
                if j<i:
                    c=c+1
            lst.append(c)
        return lst
#o(2n)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        res=[]
        sorted_nums=sorted(nums)
        for i in range(len(nums)):
            if sorted_nums[i] not in d:
                d[sorted_nums[i]]=i

        for k in nums:
            res.append(d[k])
        return res  
