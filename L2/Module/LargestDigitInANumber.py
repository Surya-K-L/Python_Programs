s=int(input())
p=0
while(s>0):
    k=int(s%10)
    if(k>p):
        p=k
    s=int(s/10)
print(p)
