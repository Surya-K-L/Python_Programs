# Write a program to reverse a given number.
# For example:

# Input	Result
# 25      52
# 5       5


n=int(input())
m=0
while(n>0):
    t=n%10
    m=(m*10)+t
    n=int(n/10)
print(m)