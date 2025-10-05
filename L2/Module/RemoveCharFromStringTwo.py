n=int(input())
s1=input()
s2=input()
for i in range(len(s2)):
    k=s2[i]
    s1=s1.replace(k,"")
print(s1)
