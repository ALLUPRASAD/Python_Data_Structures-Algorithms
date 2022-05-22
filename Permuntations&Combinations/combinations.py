def tostring(st):
    return " ".join(st)
def permut(a,l,r):
    if l==r:
        print(tostring(a))
    for i in range(l,r+1):#0,3,i=0
        a[l],a[i]=a[i],a[l]#
        permut(a,l+1,r)# 1,3
        a[l],a[i]=a[i],a[l]
    
string = "asx"
n = len(string)
a = list(string)
permut(a, 0, n-1)  


# write a code to Print all combinations of x 
# output example: rkishna,shnairk

x="abc"

def permute(x):
  result = []
  if len(x) == 0:
    return []
  
  if len(x) == 1:
    return [x]
  
  for i in range(len(x)):
    for j in permute(x[:i]+x[i+1:]):
        result.append(x[i] + j)
  
  return result

permute(x)
