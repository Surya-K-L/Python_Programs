# Print the elements in the array in the reverse order.


# Input Format
# Input consists of n+1 integers. The first integer corresponds to ‘n’ , the size of the array. The next ‘n’ integers correspond to the elements in the array

# Output Format
# Refer sample output for details.

# Sample Input 1
# 5
# 9
# 3
# 5
# 4
# 3
# Sample Output 1
# 3
# 4
# 5
# 3
# 9


n=int(input())
arr=[]
for x in range(0,n):
    arr.append(int(input()))
for x in range(n-1,-1,-1):
    print(arr[x])