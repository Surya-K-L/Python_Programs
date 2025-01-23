# Write a program that display equal positive and negative numbers for a given number

# Zero should not be displayed

# For example:

# Input	Result
# 6       3 2 1 -1 -2 -3

# 10      5 4 3 2 1 -1 -2 -3 -4 -5



n=int(input())
t=int(n/2)
s=-1
for x in range(t,0,-1):
    print(x,end=" ")
for x in range(0,t):
    print(s,end=" ")
    s-=1
        