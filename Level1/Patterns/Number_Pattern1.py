# Print the given square pattern

# For example:

# Input	Result
# 2       1 2 
#         1 2 
        
# 3       1 2 3 
#         1 2 3 
#         1 2 3 


n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print(j+1,end=" ")
    print()