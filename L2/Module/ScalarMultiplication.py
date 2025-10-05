lis=[]
for i in range(3):
    r=list(map(int,input().split()))
    lis.append(r)
k=int(input())
for i in range(3):
    for j in range(3):
        print(lis[i][j]*k,end=" ")
    print()
