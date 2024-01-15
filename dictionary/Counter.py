numbers = [1,2,3,4,5,4,3,9,9,10,10,10]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1
    
print (frequency)