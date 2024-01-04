# xor has associative property not required sorting 1^1=0,1^2=2^1,0^1=0.
def unique(x):
    ans=0
    for i in range(len(x)):
        ans=ans^x[i]
    return ans


if __name__ == "__main__":
    x=[1,2,1,2,7,8,9,7,9,9,9,9]
    dd=unique(x)
    print(dd)


