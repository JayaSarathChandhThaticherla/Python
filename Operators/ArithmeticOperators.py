'''Below are the Arithmetic operators and their functions
      +     (Addition)
      -     (Subtraction)
      *     (Multiplication)
      %     (Modulus)
      /     (Divison)
      //    (Floor Divison)
      **    (Power)

 '''

class ArithmeticOperators:
    def __init__(self,A,B):
        self.a=A
        self.b=B

#This function is used to add 2 integers
    def Add(self):  
        print("The Addition is ",self.a+self.b)

#This function is used to Sutract b from a
    def Sub(self):
        print("The Subtraction is ",self.a-self.b)

#This function is used to Multiply 2 integers
    def Multiplication(self):
        print("The Multiplication is ",self.a*self.b)

#This function is used to print the reminder 
    def Modulus(self):
        print("The Reminder is ",self.a%self.b)

#This funcyion is a simple divison
    def divison(self):
        print("The divison is ",self.a/self.b)

#This function is used for floor divison
    def FloorDivison(self):
        print("The FloorDivison is ",self.a//self.b)

#This function is used for a integer
    def Power(self):
        print("The Power is ",self.a**self.b)
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
obj=ArithmeticOperators(a,b)
obj.Add()
obj.Sub()
obj.Multiplication()
obj.Modulus()
obj.divison()
obj.FloorDivison()
obj.Power()

    
