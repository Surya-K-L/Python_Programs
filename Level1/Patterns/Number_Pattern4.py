# Write a program to display the pattern given below.

# For example:

# Input	Result
# 5       1
#         2 2
#         3 3 3
#         4 4 4 4
#         5 5 5 5 5


n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print(i+1,end=" ")
    print()