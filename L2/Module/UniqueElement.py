n=int(input())
p=0
lis=[0]*100
for i in range(n):
    t=int(input())
    lis[t]+=1
k=0
for i in range(100):
    if(lis[i]==1):
        k=1
        print(i)
        break
if(k==0):
    print("No unique elements")
