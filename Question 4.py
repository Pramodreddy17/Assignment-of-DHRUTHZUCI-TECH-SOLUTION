x=int(input("Enter size of list"))
ini_list = []
for i in range(0,x):
    ini_list.append(input())
result = sorted(ini_list, key = ini_list.count,reverse = True)
x=result[-1]
print(x)