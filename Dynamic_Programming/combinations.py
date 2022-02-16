def combinations(str,max_len):
  if len(str)==0:
    print(max_len)
    return
  for i in range(len(str)):
    ch=str[i]
    left=str[0:i]
    right=str[i+1:]
    result=left+right
    combinations(result,max_len+ch)
    
str='prasad'
max_len=''
combinations(str,max_len)
