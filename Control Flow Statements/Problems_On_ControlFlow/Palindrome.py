class Palindrome:
    def __init__(self,num):
        self.n=num
    def Logic(self):
        pal=0
        z1=self.n
        while(self.n>0):
            rem=self.n%10
            pal=(pal*10)+rem
            self.n=self.n//10
        if pal==z1:
            return pal
        else:
            return None
N=int(input("enter the number you want to check for palindrome : "))
obj=Palindrome(N)
x=obj.Logic()
if x==None:
    print(N,"Not a palindrome")
else:
    print(N,"is a palindrome")

