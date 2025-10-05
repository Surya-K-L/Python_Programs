lis=list(map(int,input().split()))
ind=int(input())
num=int(input())
for i in range(len(lis)):
    if(i==ind-1):
        print(num,end=" ")
        print(lis[i],end=" ")
    else:
        print(lis[i],end=" ")
