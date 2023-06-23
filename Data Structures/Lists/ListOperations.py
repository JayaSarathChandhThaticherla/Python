'''
List Operations 
1.append adds an element at the end
2.extend  adds a new list to the existing list
3.insert  inserts a new element at the desired position
4.remove  removes the 1st element with the same name
5.pop     removes the element at the specified position
6.sort    sorts the elements in a order
7.reverse reverse the List
8.slice   slices the List same as a string
9.len    checks the length of the List
10.min  
11.max
12.count
13.concatenate
14.index
15.clear

'''

class Lists:
    def __init__(self,List):
        self.l=List
    def appends(self):
        self.l.append('hero')
        return self.l
        
    def extend(self):
        self.l.extend(['dan','miguel'])
        return self.l
    def insert(self):
        self.l.insert(0,'stan')
        print(self.l)
    def remove(self):
        self.l.remove('sarath')
        return self.l
    def pop(self):
        self.l.pop(1)
        print(self.l)
    def reverse(self):
        self.l.reverse()
        print(self.l)
    def sort(self):
        self.l.sort()
        print(self.l)
    def slice(self):
        print(self.l[:2])
    def length(self):
        print(len(self.l))

    def min(self):
        print(min(self.l))
    def max(self):
        print(max(self.l))
    def count(self):
        print(self.l.count(1))
    def concatenate(self):
        L2=[2,2,2,2]
        print(self.l+L2)
    def index(self):
        print(self.l.index(8))
    def clear(self):
        print(self.l.clear())

# L=['sam','Hans','sarath']
L=[7,3,8,1,1]
obj=Lists(L)
print(obj.remove())
print(obj.extend())
print(obj.appends())
obj.pop()
obj.insert()
obj.reverse()
obj.sort()
obj.slice()
obj.length()
obj.min()
obj.max()
obj.count()
obj.concatenate()
obj.index()
obj.clear()