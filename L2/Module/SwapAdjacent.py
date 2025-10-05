n=int(input())
lis=[]
for i in range(n):
    lis.append(int(input()))
for i in range(0,n,2):
    t=lis[i]
    lis[i]=lis[i+1]
    lis[i+1]=t
print(*lis)
    
