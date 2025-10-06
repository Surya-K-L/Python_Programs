s=input().split(" ")
for i in range(len(s)):
    k=s[i]
    if(":" in k):
        p=s[i].split(":")
        print(p[2])
