# Exercise 1) Sum of Numbers
sum = 0
for number in range(10):
    sum += number
print(sum)
print('\n')

#Exercise 2) Largest Number
large = 0
for number in range(10):
    if number >= large:
        large = number  
    if number < large:   
        large = large
print(large)
print('\n')

#Exercise 3) Smallest Number
small = 0 
for number in range(10):
    if number <= small:
        small = number
    if number >= small:
        number = number
print(small)
print('\n')

#Exercise 4) Even Numbers
for number in range(10):
    if number%2 == 0 and number != 0:
        print(number)
print('\n')

#Exercise 5) Positive Numbers
for number in range(-10,10):
    if number > 0:
        print(number)
print('\n')

#Exercise 6) Positive Number 2  LIKED!
new_list= []
for number in range(-10,10):
    if number >0:
        new_list.append(number)
print(new_list)  
print('\n')

#Exercise 7) Multiply a list
mulitpier = 3
new_list = []
for number in range(100):
    number *= mulitpier 
    new_list.append(number)
print(new_list) 
print('\n')

#Exercise 8) Multiply Vectors  LIKED
new_list =[]
list_one = range(10)
list_two = range(10)
for number in range(10):   
    new_list.append(list_one[number]*list_two[number]) 
    number+=1
print(new_list) 
print('\n')

#Exercise 9) Matrix Addition   LIKED
matrix_one = [[1,1,1],[2,3,1]]
matrix_two = [[4,1,1],[2,2,2]]
new_matrix = [[0,0,0],[0,0,0]]
for i in range(len(matrix_one)):      #checking row(s) (checking how many brackets)
    for j in range(len(matrix_one[0])):   #checking column(s) (checking how many values within brack)
        new_matrix[i][j] = matrix_one[i][j] + matrix_two[i][j] #adds matrix 1 with matrix 2       
print(new_matrix)
print('\n')

#update to exercise 9/10 to print out actually maxtrix setup
matrix_one = [[1,2,3],[1,2,3]]
matrix_two = [[1,2,3],[1,5,3]]
new_matrix = [0,0,0],[0,0,0]
for i in range(len(matrix_one)):  #2
    for j in range(len(matrix_one[0])):   #3
        new_matrix[i][j] = matrix_one[i][j] + matrix_two[i][j]
print(f'{new_matrix[:1]}\n{new_matrix[1:]}\n')


#Exercise 10) Matrix Addition 2
matrix_one = [[1,1],[2,2]]
matrix_two = [[1,1],[2,2]]
new_matrix = [[0,0],[0,0]]
for i in range(len(matrix_one)):      #checking row
    for j in range(len(matrix_one[0])):   #checking column
        new_matrix[i][j] = matrix_one[i][j] + matrix_two[i][j] #adds matrix 1 with matrix 2       
print(new_matrix)
print('\n')

#Exercise 11) De-dup
list = [1,4,23,354,2,3,4,2,0,10]
new_list = []
list.sort()
j = 0
for i in range(len(list)):
    if list[i-1] != list[j]:
        new_list.append(list[i])      
    j = j+1
print(new_list)  
print('\n')


#Exercise Bonus: Matrix Multiplication
matrix_one=[[0,1],[2,3]]
matrix_two=[[0,1],[2,3]]
new_matrix=[[0,0],[0,0]]

for i in range(len(matrix_one)): #length 2 Rows
        for j in range(len(matrix_two[0])): #length 2 Columns
                new_matrix[i][j] = matrix_one[i][j] * matrix_two[i][j]
print(new_matrix)                

    
    


    
