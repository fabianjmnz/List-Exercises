list = [1,4,23,354,2,3,4,2,0,10]
new_list = []
list.sort()
j = 0
for i in range(len(list)):
    if list[i-1] != list[j]:
        new_list.append(list[i])      
    j = j+1
print(new_list)