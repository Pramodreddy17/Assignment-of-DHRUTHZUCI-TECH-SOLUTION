x= int(input("Enter the size of first array: "))
y= int(input("Enter the size of second array: "))
list1=[]
for i in range(0,x):
    a=int(input())
    list1.append(a)
list2=[]
for i in range(0,y):
    a=int(input())
    list2.append(a)
b=set()
for i in range(0,x):
    b.add(list1[i])
c=set()
for i in range(0,y):
    c.add(list2[i])
intersection = b.intersection(c)
print(intersection)
