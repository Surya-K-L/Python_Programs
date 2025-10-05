n=int(input())
lis=[0]*n
for i in range(n):
    lis[i]=int(input())
s=0
for i in range(n):
    for j in range(i+1,n):
        if(lis[j]==lis[i]):
            s=1
            print(lis[i])
            break
    if(s==1):
        break
if(s==0):
    print("No repeating elements")
