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
