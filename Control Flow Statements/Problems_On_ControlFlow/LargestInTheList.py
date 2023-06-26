List=[7,1,2,11,9]
#The right way
L1=len(List)    
for x in range(L1):
    min=x
    for y in range(x+1,L1):
        if List[min]>List[y]:
            min=y
    temp=List[min]
    List[min]=List[x]
    List[x]=temp
print(List[-1],"is the biggest element")



#Simple way
# z=0
# for x in List:
#     if x>z:
#         z=x
# print('the largest element is :',z)
    