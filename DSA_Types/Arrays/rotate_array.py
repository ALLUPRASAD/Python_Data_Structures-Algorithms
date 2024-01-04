class Solution(object):
    def rotate(self,matrix):
        N=len(matrix)
        for i in range(N//2+N%2):
            for j in range(N%2):
                temp=matrix[N-j-1][i]
                matrix[N-j-1][i]=matrix[N-i-1][N-j-1]
                matrix[N-i-1][N-j-1]=matrix[j][N-1-i]
                matrix[j][N-1-i]=matrix[i][j]
                matrix[i][j]=temp
