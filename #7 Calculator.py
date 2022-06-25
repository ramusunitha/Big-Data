class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def addition(self):
        print(self.a+self.b)
        
    def subtraction(self):
        print(self.a-self.b)
    
    def multiplication(self):
        print(self.a*self.b)

calcobj=calculator(10,5)
calcobj.addition()
calcobj.subtraction()
calcobj.multiplication()