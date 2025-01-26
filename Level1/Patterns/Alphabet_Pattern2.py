# Write a program to print the following pattern for a given value of n

# For example:

# Input	Result
# 3       A 
#         B C 
#         D E F 

# 4       A 
#         B C 
#         D E F 
#         G H I J 

n=int(input())
t=65
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(t),end=" ")
        t+=1
    print()
