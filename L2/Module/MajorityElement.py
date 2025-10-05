n=int(input())
c=0
lis=[]
for i in range(n):
    lis.append(int(input()))
lis.sort()
i=0
f=0
while(i<len(lis)):
    c=1
    while(i<len(lis)-1 and lis[i]==lis[i+1]):
        c+=1
        i+=1
    if(c>n//2):
        print(lis[i])
        f=1
    i+=1
if(f==0):
    print(0)
    
