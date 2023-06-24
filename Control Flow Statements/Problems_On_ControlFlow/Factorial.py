# Factorial of a given number

#4! = 1x2x3x4

class Factorial:
    def __init__(self,N):
        self.n=N
    def logic(self):
        z=1
        for x in range(1,self.n+1):
            z=z*x
        print(z)
Number=int(input("enter the number you want to find the factorial for : "))
obj=Factorial(Number)
obj.logic()