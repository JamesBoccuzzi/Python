import random
random_num = random.randrange(1,5)
print(random_num)
number = int(input("pick a number between 1-5 "))
if number == random_num:
    print("You have selected the correct number")
else:
    print("You have not selected the correct number")
    
    