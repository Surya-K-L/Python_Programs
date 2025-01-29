# Develop a program to interchange the first and last elements in the Array.

# Input Format:

# The first line of input N denotes the size of the list followed by N integers.

# For example:

# Input	                Result
# 8
# 1 29 51 9 17 6 7 23     23 29 51 9 17 6 7 1

# 5
# 1 2 3 4 5               5 2 3 4 1


n=int(input())
arr=list(map(int,input().split()))
for x in range(0,n):
    if(x==0):
        print(arr[n-1],end=" ")
    elif(x==n-1):
        print(arr[0],end=" ")
    else:
        print(arr[x],end=" ")