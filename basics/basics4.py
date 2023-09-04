import random
random_num = random.randrange(1,10)
print(random_num)
number = int(input("pick a number between 1-10 "))
attemps = 0
while attemps < 3:
    attemps = attemps + 1
    if number == random_num:
        print("You have selected the correct number")
    elif number > random_num:
        print("The number you have selected is too large")
    else:
        print("The number you have selected is too small")
    number = int(input("pick a new number between 1-10 "))

    
    