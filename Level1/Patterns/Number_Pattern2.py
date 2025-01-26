# Print the given pattern for a given number

# For example:

# Input	Result
# 3       1 1 1 
#         2 2 2 
#         3 3 3 
        
# 4       1 1 1 1 
#         2 2 2 2 
#         3 3 3 3 
#         4 4 4 4 
        
# 5       1 1 1 1 1 
#         2 2 2 2 2 
#         3 3 3 3 3 
#         4 4 4 4 4 
#         5 5 5 5 5 


n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print(i+1,end=" ")
    print()