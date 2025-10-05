n=int(input())
lis=list(map(int,input().split()))
z=0
for i in range(1,n,1):
    if(i not in lis):
        z=1
        print(i)
        break
if z==0:
    print(-1)
