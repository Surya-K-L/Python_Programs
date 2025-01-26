# Write a program to print numbers between 2 given numbers

# For example:

# Input	Result
# 3       3 4 5 
# 5

# 1       1 2 3 4 5 6 7 
# 7

n=int(input())
m=int(input())
for x in range(n,m+1):
    print(x,end=" ")

