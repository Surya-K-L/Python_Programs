s=list(map(int,input().split(",")))
l=[0]*25
for i in range(len(s)):
    l[s[i]]+=1
ans=[]
for i in range(25):
    if(l[i]>0):
        ans.append(i)
for i in range(len(ans)):
    if(i<len(ans)-1):
        print(ans[i],end=",")
    else:
        print(ans[i])
