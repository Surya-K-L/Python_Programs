# Write a program to find sum of all odd numbers from 1 to n.

# For example:

# Input	Result
# 15      Sum of Odd Numbers from 1 to 15: 64

n=int(input())
print(f"Sum of Odd Numbers from 1 to {n}: ",end="")
s=0
for t in range(1,n+1,1):
    if(t%2==1):
        s+=t
print(s)