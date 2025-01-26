# Write a program to add all digits of a given number

# For example:

# Input	Result
# 345     12
# 30      3

n=int(input())
s=0
while(n>0):
    t=n%10
    s+=t
    n=int(n/10)
print(s)
