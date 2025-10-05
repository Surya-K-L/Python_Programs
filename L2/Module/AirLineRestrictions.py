n=int(input())
for i in range(n):
    li=list(map(int,input().split()))
    t1=li[0]+li[1]
    t2=li[0]+li[2]
    t3=li[1]+li[2]
    c1=li[2]
    c2=li[1]
    c3=li[0]
    if((t1<=li[3] and c1<=li[4]) or(t2<=li[3] and c2<=li[4]) or(t3<=li[3] and c3<=li[4])):
        print("YES")
    else:
        print("NO")
