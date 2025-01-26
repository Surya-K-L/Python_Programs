# Write a program to print the current pattern

# For example:

# Input	  Result
# 3       1 
#         1 1 
#         1 1 1 

# 5       1 
#         1 1 
#         1 1 1 
#         1 1 1 1 
#         1 1 1 1 1 

n=int(input())
t=1
for i in range(0,n):
    for j in range(0,i+1):
        print(t,end=" ")
    print()
