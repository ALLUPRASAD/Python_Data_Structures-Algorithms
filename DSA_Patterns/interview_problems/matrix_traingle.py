def triangle_matrix(array):
    matrix = [[0 for i in range(array)] for j in range(array)]
    x = len(matrix)
    y = len(matrix[0])


    for m in range(x):
        k = 1
        for n in reversed(range(y - m-1, y)):
            print(m,n)
            matrix[n][m] = k
            k += 1

    return matrix

if __name__ == "__main__":
    array = 8
    results = triangle_matrix(array)
    for row in results:
        print(row)
