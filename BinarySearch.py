class BinarySearch:
    def __init__(self,List):
        self.List=List
    def Logic(self,first,last,target):
        while(first<=last):
            mid=(first+last)//2
            x1=self.List[mid]
            if x1==target:
                return mid
                break
            elif target<x1:
                last=mid-1
            elif target>x1:
                first=mid+1
List=[21,22,23,24,25,26,27]
first=0
last=len(List)
target=int(input("enter the element you want to search for : "))
# target=27
obj=BinarySearch(List)
x=obj.Logic(first,last,target)
if x!=None:
    print('the element',target, 'is found at',x)
else:
    print('element not found in the list')
    

