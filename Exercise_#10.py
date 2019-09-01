matrix_one = [[1,1],[2,2]]
matrix_two = [[1,1],[2,2]]
new_matrix = [[0,0],[0,0]]
for i in range(len(matrix_one)):      #checking row
    for j in range(len(matrix_one[0])):   #checking column
        new_matrix[i][j] = matrix_one[i][j] + matrix_two[i][j] #adds matrix 1 with matrix 2       
print(new_matrix)