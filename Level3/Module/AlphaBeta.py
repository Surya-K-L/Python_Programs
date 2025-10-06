n=int(input())
lis=[]
total=0
for i in range(n):
    lis.append(input())
s=input()
for i in range(n):
    p=lis[i]
    if(p[0]==s):
        k=lis[i].split()
        su=int(k[1])
        total+=su
print(total)
