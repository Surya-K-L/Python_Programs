# Write a program to Find the greatest number among three numbers.

a,b,c=map(int,input().split())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)