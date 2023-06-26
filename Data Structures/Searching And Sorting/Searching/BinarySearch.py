
def Logic():
    List=[0,1,2,3,4,5,6,7,8,9]
    target=77
    ls=0
    le=len(List)-1
    while(ls<=le):
        mid=(ls+le)//2
        if List[mid]==target:
            return 0
        elif List[mid]>target:
            le=mid-1
        elif List[mid]<target:
            ls=mid+1
if Logic()!=None:
    print('element found')
else:
    print("not")

