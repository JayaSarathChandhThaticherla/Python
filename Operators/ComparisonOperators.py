'''
==  Equals to
>   Greater than
<   Less Than
>=  Greater than or equal to
<=  Less than or equal to
!=  Not equal to

'''

class ComparisonOPerators:
    def __init__(self,a,b):
        self.a=a
        self.b=b

#This Function is used for Equals to
    def equalsto(self):
        if self.a==self.b:
            print("Both are equal")
#This Function is used for Greater than
    def Greaterthan(self):
        if self.a>self.b:
            print("a is greater than b")
#This Function is used for Less Than
    def Lessthan(self):
        if self.a<self.b:
            print("a is less than b")
#This Function is used for Greater than or equal to
    def GreaterorEqual(self):
        if self.a>=self.b:
            print("a is greater than or equal to b")
#This Function is used for Less than or equal to
    def Lessorequal(self):
        if self.a<=self.b:
            print("a is less than or equal to b")
#This Function is used for Not equal to
    def Notequal(self):
        if self.a!=self.b:
            print("a and b are not equal")
x=1
y=3
obj=ComparisonOPerators(x,y)
obj.equalsto()
obj.Greaterthan()
obj.Lessthan()
obj.GreaterorEqual()
obj.Lessorequal()
obj.Notequal()