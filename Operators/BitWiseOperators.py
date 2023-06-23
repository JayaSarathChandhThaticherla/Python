'''
& and
| or
~ not
'''


# Examples of Bitwise operators
a = 10
b = 4
class BitwiseOperators():
    def __init__(s,a,b):
        s.a=a
        s.b=b
    
    def Logic(self):
        # Print bitwise AND operation
        print(a & b)
        
        # Print bitwise OR operation
        print(a | b)
        
        # Print bitwise NOT operation
        print(~a)
        
        # print bitwise XOR operation
        print(a ^ b)
        
        # print bitwise right shift operation
        print(a >> 2)
        
        # print bitwise left shift operation
        print(a << 2)

obj=BitwiseOperators(a,b)
obj.Logic()