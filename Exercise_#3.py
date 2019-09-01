small = 0 
for number in range(10):
    if number <= small:
        small = number
    if number >= small:
        number = number
print(small)