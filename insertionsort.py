n=int(input("Enter the number of elements:"))
list=[]
for i in  range(n):
    value=int(input("Enter the value:"))
    list.append(value)
print(list)
for i in range(0,n):
    key=list[i]
    j=i-1
    while(j>0 and list[j]>key):
        list[j+1]=list[j]
        j=j-1
    list[j+1]=key
print("sorted list:")
print(list)
