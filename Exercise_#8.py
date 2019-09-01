new_list =[]
list_one = range(10)
list_two = range(10)
for number in range(10):   
    new_list.append(list_one[number]*list_two[number]) 
    number+=1
print(new_list) 