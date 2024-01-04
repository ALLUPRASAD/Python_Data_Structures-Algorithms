
#brute_force 

# str='xrrdfsdvdfvfb'
# max_s=0
# for i in range(len(str)):
#     for j in range(len(str)+1):
#         sub_string=str[i:j]
#         if sub_string!='':
#             if (sub_string[0]==sub_string[-1]):
#                 max_s=max(max_s,len(str[i:j]))
# print(max_s)


class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        max_len=0
        c={}
        d={}
        if len(s)<=2:
            return 0 
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                c[s[i]]=i
        for k in c.keys():
            substrings=s[d[k]:c[k]]
            max_len=max(max_len,len(substrings))
        return max_len-1
