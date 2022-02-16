
#brute_force 

str='xrrdfsdvdfvfb'
max_s=0
for i in range(len(str)):
    for j in range(len(str)+1):
        sub_string=str[i:j]
        if sub_string!='':
            if (sub_string[0]==sub_string[-1]):
                max_s=max(max_s,len(str[i:j]))
print(max_s)
