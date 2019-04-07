list1=input()
list2=input()
for i in list1:
    x=0
    while list1.index(list2[x])>0:
        list1.remove(list2[x])
    x+=1
print(list1)