s=input()
n=input()
k=int(input())
c=0
id=-1
for i in range(len(s)):
    if(s[i]==n and c!=k):
        c+=1
        id=i
print(id)
