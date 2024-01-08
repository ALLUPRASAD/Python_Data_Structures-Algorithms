matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
m = len(matrix)
n = len(matrix[0])
filt=[]
for i in range(m):
    for j in range(n):
        if matrix[i][j]==0:
            filt.append([i,j])
for x,y in filt:
    print(x,y)
    for row in range(n):
        print(x,row)
        matrix[x][row]=0
    for col in range(m):
        print(col,y)
        matrix[col][y]=0
print(matrix)


