n=int(input())
lis=[]
for i in range(n): lis.append(int(input()))
k=int(input())
s=-1
e=-1
f=0
for i in range(n):
    for j in range(i,n):
        if(i!=j and lis[i]+lis[j]==k):
            s=i
            e=j
            f=1
            break;
    if(f==1):
        break
if(f==1):
    print("Index1:",s)
    print("Index2:",e)
else:
    print("No two sum solution")
