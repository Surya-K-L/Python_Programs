# Write a program to add only the positive elements in the array

# For example:

# Input	                  Result
# 5                         90
# 10 -20 30 -40 50

# 6
# 10 20 30 -40 -50 -60      60



n=int(input())
arr=list(map(int,input().split()))
t=0
for i in range(0,n):
     if(arr[i]>0):
        t=t+arr[i]
print(t)