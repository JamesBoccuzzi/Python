a = dict()
b = {}
c = {'James' : 'Boccuzzi',
     'computer' : 'science'}
print(c.keys())
print(c.values())
print(c.items())

for key in c.keys():
    print(key)
    
for value in c.values():
    print(value)
    
for key, value in c.items():
    print(key, " ", value)
    
c['vito'] = 'gentile'

for key, value in c.items():
    print(key, " ", value)
    
n = {}
for num in range(1,6):
    n[num] = num * num
    
print(n)