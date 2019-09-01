large = 0
for number in range(10):
    if number >= large:
        large = number  
    if number < large:   
        large = large
print(large)