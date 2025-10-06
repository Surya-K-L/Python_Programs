n=int(input())
for i in range(n):
    k=int(input())
    lis=list(map(int,input().split()))
    for j in range(k):
        min=100000
        for z in range(k):
            for x in range(k):
                if(z!=x):
                    t=abs(lis[z]-lis[x])
                    if(t<min):
                        min=t
    print(min)
