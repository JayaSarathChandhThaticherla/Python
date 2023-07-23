class Multiplication:
    def __init__(self,Number):
        self.n=Number
    def Logic(self):
        for x in range(1,11):
            print(self.n,"X",x," =",self.n*x)
X1=int(input("enter the number for the Multiplication table : "))            
obj=Multiplication(X1)
obj.Logic()