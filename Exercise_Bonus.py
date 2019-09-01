matrix_one=[[0,1],[2,3]]
matrix_two=[[0,1],[2,3]]
new_matrix=[[0,0],[0,0]]

for i in range(len(matrix_one)): #length 2 Rows
        for j in range(len(matrix_two[0])): #length 2 Columns
                new_matrix[i][j] = matrix_one[i][j] * matrix_two[i][j]
print(new_matrix)