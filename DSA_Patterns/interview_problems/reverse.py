
# reversing with o(n) with out extra space
class rever:

    def reverser(self,array):
        
        m=len(array)
        for i in range(0,m//2):
            array[i],array[m-i-1]=array[m-i-1],array[i]
        return array
    def old_swap(self,array):
        m=len(array)
        for i in range(0,m//2):
            temp=array[i]
            array[i]=array[m-i-1]
            array[m-i-1]=temp
        return array
if __name__=="__main__":
    instance_of_rever = rever()
    array = [1, 2, 3, 5, 1, 2, 7, 8, 9]
    results = instance_of_rever.old_swap(array)
    print(results)