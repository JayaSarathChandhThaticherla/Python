# Write a Python program to find the sum of all even numbers between 1 and 100 (inclusive)
class Sum:
    def __init__(self,Number):
        self.n=Number
    def Logic(self):
        sum=0
        for x in range(1,self.n):
            if x%2==0:
                sum=sum+x
        print("The sum of all even numbers between 1 and 100 is :",sum)
Number=101 #here we used the end value as 101 because we want the 100 included
obj=Sum(Number)
obj.Logic()


