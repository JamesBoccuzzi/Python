a = []
a.append(1)

print(a)

b = []
for number in range(-10,10):
    b.append(number)

print(b)
b.sort()
print(b)

b.insert(2,39)
print(b)

c = [62,53,124]

b.extend(c)
print(b)

b.reverse()
print(b)

b.pop(5)
print(b)

b.remove(62)
print(b)