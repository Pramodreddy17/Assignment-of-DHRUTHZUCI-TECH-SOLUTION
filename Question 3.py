a=input("Enter string")
a1, a2, a3, a4, a5, a6=0,0,0,0,0,0
if(a==""):
    print("true")
else:
    for i in range(0, len(a)):
        if(a[i]=='('):
            a1+=1
        elif(a[i]==')'):
            a2+=1
        elif(a[i]=='{'):
            a3+=1
        elif(a[i]=='}'):
            a4+=1
        elif(a[i]=='['):
            a5+=1
        elif(a[i]==']'):
            a6+=1
        else:
            print("false")  
    if(a1==a2 and a3==a4 and a5==a6):
        print("true")
    else:
        print("false")
