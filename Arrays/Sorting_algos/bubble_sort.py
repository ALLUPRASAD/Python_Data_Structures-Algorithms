def bubble(x):
    for i in range(len(x)):
        for j in range(0,len(x)-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x
x=[1,4,45,6,3,4,5,99]
bubble(x)
