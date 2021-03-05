def findSingle( ar, n):
    res = ar[0]
    for i in range(1,n):
        res = res ^ ar[i]
    return res
ar = [4,1,2,1,2]
print(findSingle(ar, len(ar)))
