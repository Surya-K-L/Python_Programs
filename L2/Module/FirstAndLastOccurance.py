n=int(input())
lis=[]
for i in range(n):
    lis.append(int(input()))
k=int(input())
s=-1
e=-1
for i in range(n):
    if(lis[i]==k):
        if(s==-1):
            s=i
        e=i
print(s,e)
