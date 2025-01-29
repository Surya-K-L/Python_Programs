# Develop a program to print primary/principal and secondary/anti-diagonal diagonals of a matrix.

# Example: Consider a matrix, { { 1, 5, 8 } , { 4, 3, 1 } , { 6, 5, 2 } }. Primary/Principal and secondary/Anti-diagonal elements are as follows,

# Program to find the sum of diagonal elements of a 2D array

# For example:

# Input	Result
# 2       Primary diagonal elements:
# 2       1
# 1       4
# 2       Secondary diagonal elements:
# 3       2
# 4       3

# -2      Row and column size should not be negative
# -2


n=int(input())
m=int(input())
if(n<0 and m<0):
    print("Row and column size should not be negative")
elif(n!=m):
    print("Row and column size should be same")
else:
    arr=[]
    for i in range(n):
        col=[]
        for j in range(m):
            t=int(input())
            col.append(t)
        arr.append(col)
    print("Primary diagonal elements:")
    for i in range(n):
        for j in range(m):
            if(i==j):
                print(arr[i][j])
    print("Secondary diagonal elements:")
    for i in range(n):
        for j in range(m):
            if(i+j==n-1):
                print(arr[i][j])
                