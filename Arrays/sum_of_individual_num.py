#1st method
def input_num(num):
    s=0
    x=num
    while x>0:
        y=x%10
        x=x//10
        s=s+y
    return s
  
  # recursive approach
  
def addDigits(num):
    nums = list(map(int, str(num)))
    if len(nums)>1:
        nums = sum(nums)
        nums = addDigits(nums)
    else:
        nums = nums[0]
    return nums
