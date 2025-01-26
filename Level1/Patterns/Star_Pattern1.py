# Print the given  pattern

# For example:

# Input	Result
# 2       * * 
#         * * 

# 3       * * * 
#         * * * 
#         * * * 

n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    print()
