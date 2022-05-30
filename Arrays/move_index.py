
def move_ones(nums):
    index=0
    for num in nums:
        if num!=1:
            nums[index]=num
            index=index+1
    for nu in range(index,len(nums)):
        nums[nu]=1
    return nums
  
#   input:nums=[1,1,0,8,7,6,5]
#   move_ones(nums)
#   output:[0, 8, 7, 6, 5, 1, 1]
