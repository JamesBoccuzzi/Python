a = [2,5,8,11,24,9,14]
b = [1,2,4,8,11,24]
c = []
for number_a in a:
    for number_b in b:
        if number_a == number_b:
            c.append(number_b)
print(c)

