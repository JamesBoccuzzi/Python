class stack:
    def __init__(self):
        self.data = []
        
    def __str__(self):
        s =''
        for num in self.data:
            s = s + str(num) + ' '
        return(s)
    
    def append(self,num):
        self.data.append(num)

    def pop(self):
        return(self.data.pop())
                 
s = stack()
s.append(3)
s.append(5)
s.append(7)

print(s)
print(s.pop())



