class NaturalNumbers:
    def __init__(self,Num):
        self.Num=Num
    def Logic(self):
        for x in range(1,self.Num+1):
            print(x,end=" ")
Range=int(input("enter the number you want to print natural numbers upto : "))
obj=NaturalNumbers(Range)
obj.Logic()