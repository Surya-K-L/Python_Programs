# Write a program to read n numbers and display the numbers in reverse order

# Input:
# 5
# 10 30 20 50 43

# Output:
# 43 50 20 30 10

# For example:

# Input	            Result
# 5                   50
# 10 20 40 30 50      30
#                     40
#                     20
#                     10

n=int(input())
arr=list(map(int,input().split()))
for x in range(n-1,-1,-1):
    print(arr[x])