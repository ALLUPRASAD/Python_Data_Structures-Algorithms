
# head_recursion
#A recursive function is tail recursive when recursive call is the last thing executed by the function. For example the following Python function factorial() is tail recursive.
1.factorial

def head_rec(n,nums=1):
    if n>0:
        return head_rec(n-1,n*nums)
    else:
        return nums
2.fibnochi

def feb(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        feb1=feb(n-1)
        feb2=feb(n-2)
        return feb1+feb2
feb(10)

#Tail_recursion

1.factorial

def tail_rec(n,num=1):
    if n==0:
        return num
    else:
        return tail_rec(n-1,num*n)
      
2.fibnochi

def fibonacci_tail(n,a=0,b=1):
    
    if n==0: return a;
    if n==1: return b;
 
    return fibonacciTail(n-1,b,a+b);
