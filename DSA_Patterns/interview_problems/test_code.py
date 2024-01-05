class testing:
    def spiral_order(matrix):
        result = []
        left,right,top,bottom=0,len(matrix)-1,0,len(matrix[0])-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top=top+1
            for j in range(top,bottom+1):
                result.append(matrix[j][right])
            right=right-1
        
            for k in range(right,left-1,-1):
                result.append(matrix[bottom][k])
            bottom=bottom-1
            for l in range(bottom,top-1,-1):
                result.append(matrix[l][left])
            left=left+1


        return result
    def reverser(array):
        
        m=len(array)
        for i in range(0,m//2):
            array[i],array[m-i-1]=array[m-i-1],array[i]
        return array
    # def rotate(matrix): 
    #     m=len(matrix)
    #     n=len(matrix[0])
    #     for i in range(m//2):
    #         for j in range(n//2): 

    #     return matrix
    def transpose(matrix):
       
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                # print(matrix,"*"*10)
        return matrix



if __name__=="__main__":

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    xx=testing.transpose(matrix)
    print(xx)
    for i in xx:
        xxx=testing.reverser(i)
        print(xxx)