n=int(input())
lis=[]
for i in range(n):
    lis.append(int(input()))
for i in range(n):
    for j in range(i,n):
        if(lis[i]>lis[j]):
            t=lis[i]
            lis[i]=lis[j]
            lis[j]=t
print(lis[1])
