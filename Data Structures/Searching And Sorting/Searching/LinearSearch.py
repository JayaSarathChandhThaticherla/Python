List=[1,2,3,4,5,6,7,8,98]
target=int(input("enter the element you want to search for : "))
def Logic():
    for x in List:
        if x == target:
            return 0
if Logic()==0:
    print('element is found')
else:
    print('element is not found')
        