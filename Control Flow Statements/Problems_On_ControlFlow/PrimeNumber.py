#Write a Python program to check if a given number is prime or not.

class Prime:
    def __init__(self,Prime):
        self.p=Prime
    def PrimeLogic(self):
        s=2
        if self.p==0 or self.p==1: # both o and 1 are not prime numbers
            return 0
        if self.p==2: # 2 is a prime number and we are intializing with 2 so we are writing a separate case here
            return None
        while(s<self.p):
            if self.p%s==0:
                return 0
            s=s+1
x=int(input("enter the number you want to check : "))
obj=Prime(x)
y=obj.PrimeLogic()
if y==None:
    print(x,"is a prime number")
else:
    print(x,"is not a prime number")