# Write a program to print from N to 0, skip a number in between.

# For example:

# Input	Result
# 8       8 6 4 2 0

# 7       7 5 3 1


n=int(input())
for x in range(n,-1,-2):
    print(x,end=" ")

