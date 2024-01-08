class Robot:
    
    def __init__(self,name):
        self.name = name
    
    def moveforward(self):
        print (self.name,'move forward')
        
R = Robot('James')
R.moveforward()