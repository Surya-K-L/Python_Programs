# Check if all elements in the array are the same

# For example:

# Input	            Result
# 5                   YES
# 10 10 10 10 10

# 3                   NO
# 5 5 4

n=int(input())
arr=list(map(int,input().split()))
t=arr[0]
f=0
for i in range(n):
    if(arr[i]==t):
        continue
    else:
        f=1
        print("NO")
        break
if(f==0):
    print("YES")