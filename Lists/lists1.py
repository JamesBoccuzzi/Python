
def maximum(numbers):
    large = 0
    for number in numbers:
        if number > large:
            large = number
    return (large)

def total(numbers):
    s = 0
    for number in numbers:
        s = s + number
    return (s)

def average(numbers):
    sum = 0
    total_num = 0
    for number in numbers:
        sum = sum + number
        total_num = total_num + 1
    return(sum / total_num)

print(average([5,10,15]))