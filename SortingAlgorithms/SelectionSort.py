List=[12,29,25,8,32,17,49]
n=len(List)
def Logic():
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if List[j]<List[min]:
                min=j
        temp=List[i]
        List[i]=List[min]   
        List[min]=temp
    print(List)
print(Logic())    


