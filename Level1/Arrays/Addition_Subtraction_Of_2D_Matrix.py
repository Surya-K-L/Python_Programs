# Develop a program to print the addition and subtraction of two 2D matrices.
# The dimensions of the matrices are given as input first.

# Example:
# Input:
# 2 2
# 2 2

# 1 2
# 3 4

# 4 5
# 6 7

# Output:

# Addition:
# 5
# 7
# 9
# 11
# Subtraction:
# -3
# -3
# -3
# -3

# For example:

# Input	Result
# -2 -2   Row and column size should not be negative
# -2 -2

# 3 4     Row and column size should be same for 2 matrices
# 1 2


# 2 2     Addition:
# 2 2     5
# 1 2     7
# 3 4     9
# 4 5     11
# 6 7     Subtraction:
#         -3
#         -3
#         -3
#         -3

r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
if((r1<0 and c1<0) or (r2<0 and c2<0)):
    print("Row and column size should not be negative")
elif((r1!=r2) or (c1!=c2)):
    print("Row and column size should be same for 2 matrices")
else:
    arr1=[]
    arr2=[]
    for i in range(r1):
        row=list(map(int,input().split()))
        arr1.append(row)
    for i in range(r2):
        row=list(map(int,input().split()))
        arr2.append(row)
    print("Addition:")
    for i in range(r1):
        for j in range(c1):
            print(arr1[i][j]+arr2[i][j])
    print("Subtraction:")
    for i in range(r2):
        for j in range(c2):
            print(arr1[i][j]-arr2[i][j])
    
    
        
            

    
