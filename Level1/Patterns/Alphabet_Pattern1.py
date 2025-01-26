# Print the given square pattern

# For example:

# Input	Result
# 2       A B
#         A B 
        
# 3       A B C 
#         A B C 
#         A B C
        
n=int(input())
for i in range(0,n):
    c=65
    for j in range(0,n):
        print(chr(c),end=" ")
        c+=1
    print() 
