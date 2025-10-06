n=int(input())
for i in range(n):
    s=input().split(" ")
    t=s[0]
    k=s[1]
    lis1=[]
    lis2=[]
    for i in range(len(t)):
        lis1.append(t[i])
    for i in range(len(k)):
        lis2.append(k[i])
    lis1.sort()
    lis2.sort()
    if(lis1==lis2):
        print("True")
    else:
        print("False")
        
