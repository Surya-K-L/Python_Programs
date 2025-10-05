n=int(input())
lis=list(map(int,input().split()))
for i in range(n):
    lis[i]=lis[i]*lis[i]
lis.sort()
for k in lis:
    print(k,end=" ")
