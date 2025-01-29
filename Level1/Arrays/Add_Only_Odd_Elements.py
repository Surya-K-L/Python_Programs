# Write a program to add only odd elements in the array

# NOTE: Add an element to total only if it is an odd number

# For example:

# Input	        Result
# 5               8
# 3 4 12 5 8

# 5               25
# 1 3 5 7 9

# 5               0
# 2 4 6 8 10


n=int(input())
arr=list(map(int,input().split()))
t=0
for x in range(n):
    if(arr[x]%2==1):
        t=t+arr[x]
print(t)
