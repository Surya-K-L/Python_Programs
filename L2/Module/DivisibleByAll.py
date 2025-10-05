n = int(input())
lis = list(map(int, input().split()))
k = 0
for i in range(n):
    da= True
    for j in range(n):
        if i != j and lis[j] % lis[i] != 0:
            da = False
            break
    if da:
        k = 1
        print(lis[i])
        break 
if k == 0:
    print(-1)
