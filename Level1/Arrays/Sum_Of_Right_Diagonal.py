# Write a program to find sum of right diagonals of a matrix.

# Note: The number of rows and columns must be equal.

# For example:

# Input	        Result
# 4               Addition of the right Diagonal elements is: 113
# 21 1 54 87
# 26 35 48 95
# 15 24 47 6
# 42 15 84 10

# 2               Addition of the right Diagonal elements is: 52
# 15 48
# 10 37


n=int(input())
arr=[]
for i in range(n):
    row=list(map(int,input().split()))
    arr.append(row)
t=0
print("Addition of the right Diagonal elements is:",end=" ")
for i in range(n):
    t=t+arr[i][i]
print(t)
