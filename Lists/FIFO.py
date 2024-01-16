class queue:
    def __init__(self):
        self.data = []
        
    def __str__(self):
        s =''
        for num in self.data:
            s = s + str(num) + ' '
        return(s)

    def enqueue(self,num):
        self.data.append(num)
        
    def dequeue(self):
        self.data.pop(0)
        

q = queue()

q.enqueue(1)
    
print(q)

q.enqueue(3)

print(q)

q.enqueue(8)

print(q)

q.dequeue()

print(q)