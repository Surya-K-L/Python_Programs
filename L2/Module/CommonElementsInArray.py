n=int(input())
lis1=list(map(int,input().split()))
m=int(input())
lis2=list(map(int,input().split()))
k=int(input())
lis3=list(map(int,input().split()))
lis4=[]
for i in range(n):
    for j in range(m):
        if(lis1[i]==lis2[j]):
            lis4.append(lis1[i])
if(len(lis4)==0):
    print("NO Elements")
else:
    fin=[]
    for i in range(len(lis4)):
        for j in range(len(lis3)):
            if(lis4[i]==lis3[j]):
                fin.append(lis4[i])
    if(len(fin)>0):
        for i in range(len(fin)):
            print(fin[i],end=" ")
    else:
        print("NO Elements")
                
