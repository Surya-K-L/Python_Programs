n=int(input())
p=0
lis=list(map(int,input().split()))
for i in range(1,n):
    if(lis[i]<lis[i-1]):
        p=1
        print(i)
        break
if(p==0):
    print(-1)
