#Write a Python program to reverse a given string.

class string:
    def __init__(self,str):
        self.s=str
    def Logic(self):
        print(self.s[::-1])
str=input("enter the string you want to reverse : ")

obj=string(str)
obj.Logic()
       