
def max_count(lis):
    hash_map = {i: nums.count(i) for i in set(lis)}
    for j in hash_map.keys():
        if hash_map[j]==max(hash_map.values()):
            return [str(j)+' is '+str(hash_map[j])+str(' times repeated')]
nums=[1,2,3,4,5,5,4,5,5,3,9]
result = map(max_count, [lis])
print(list(result))


#[['5 is 4 times repeated']]
