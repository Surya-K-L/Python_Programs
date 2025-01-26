# Write a program to print the following pattern based on input n

# For example:

# Input	Result
# 3       1 
#         2 3 
#         4 5 6 

n=int(input())
t=1
for i in range(0,n):
    for j in range(0,i+1):
        print(t,end=" ")
        t+=1
    print()