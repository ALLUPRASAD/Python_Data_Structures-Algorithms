def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_rows(matrix):
    for row in matrix:
        # Using the provided reverser function
        reverser(row)

def reverser(array):
    m = len(array)
    for i in range(0, m // 2):
        array[i], array[m - i - 1] = array[m - i - 1], array[i]
    return array

def rotate_and_get_reversed_matrix(matrix):
    # Step 1: Transpose the matrix
    transpose_matrix(matrix)
    # Step 2: Reverse the rows
    reverse_rows(matrix)
    return matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = rotate_and_get_reversed_matrix(matrix)
print(reversed_matrix )
