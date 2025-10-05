n=int(input())
f=0
s=1
print(f,end=" ")
print(s,end=" ")
for i in range(2,n):
    k=f+s
    print(k,end=" ")
    f=s
    s=k
