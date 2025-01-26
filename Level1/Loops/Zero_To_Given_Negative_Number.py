# Write a program to print from 0 to given negative number

# For example:

# Input	Result
# -7      0 -1 -2 -3 -4 -5 -6 -7 


n=int(input())
k=abs(n)
for z in range(0,k+1):
    if z==0:
        print(z,end=" ")
    else:
        print(-z,end=" ")