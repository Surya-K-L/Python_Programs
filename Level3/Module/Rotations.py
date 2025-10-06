s1 = input()
s2 = input()
s3=s1
n = len(s1)
found = False

for i in range(n):
    s1 = s1[1:] + s1[0]
    if s1 == s2:
        print(s3,"and",s2,"are rotation of each other")
        found = True
        break
if not found:
    print("Not a rotation of each other")
