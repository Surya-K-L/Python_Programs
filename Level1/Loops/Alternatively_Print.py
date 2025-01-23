# Alternatively print a given number as given in the example

# For example:

# Input	Result
# 3       3 -3 2 -2 1 -1 

# 4       4 -4 3 -3 2 -2 1 -1

n=int(input())
k=n*2
z=-n
for x in range(0,k):
    if(x%2==0):
        print(n,end=" ")
        n-=1
    else:
        print(z,end=" ")
        z+=1
 
