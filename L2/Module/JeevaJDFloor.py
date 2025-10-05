n=int(input())
lis=[]
for i in range(n):
    l=list(map(int,input().split()))
    lis.append(l)
for i in range(n):
    for j in range(4):
        je=lis[i][0]/lis[i][2]
        jd=lis[i][1]/lis[i][3]
        if(je==jd):
            print("Both")
            break
        elif(je<jd):
            print("Jeeva")
            break
        else:
            print("JD")
            break
