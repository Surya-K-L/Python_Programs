# Write a program to print the pattern given below

# For example:

# Input	Result
# 3       1
#         3 5
#         7 9 11

# 4       1 
#         3 5
#         7 9 11
#         13 15 17 19

n=int(input())
t=1
for i in range(0,n):
    for j in range(0,i+1):
        print(t,end=" ")
        t+=2
    print()
