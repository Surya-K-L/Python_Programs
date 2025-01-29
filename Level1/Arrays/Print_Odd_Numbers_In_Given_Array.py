# Write a program to print the odd numbers in a given array

# Input Format
# The first line in the input contains a number of array elements N

# The next lines N contains elements of the array

# Sample Input 1
# 5
# 1
# 3
# 7
# 5
# 4
# Sample Output 1
# Odd items of the array: 1 3 7 5

# Sample Input 2
# 5
# 2
# 4
# 6
# 8
# 10
# Sample Output 2
# No Odd Elements
# For example:

# Input	Result
# 5       Odd items of the array: 1 3 7 5 
# 1
# 3
# 7
# 5
# 4

# 3       Odd items of the array: -1 -3 
# -1
# -2
# -3

# 5       No Odd Elements
# 2
# 4
# 6
# 8
# 10



n=int(input())
arr=[]
for x in range(n):
    arr.append(int(input()))
c=0
for x in range(n):
    if(arr[x]%2==1 or arr[x]%2==-1):
        c=c+1
if(c==0):
    print("No Odd Elements")
else:
    print("Odd items of the array:",end=" ")
    for x in range(n):
        if(arr[x]%2==1 or arr[x]%2==-1):
            print(arr[x],end=" ")