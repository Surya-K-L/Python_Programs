# Display the sum of the first column in a 2D Matrix

# For example:

# Input	Result
# 2 2     12
# 5
# 6
# 7
# 8

# 2 2     40
# 10
# 20
# 30
# 40


n,m=map(int,input().split(" "))
arr=[]
for i in range(n):
    col=[]
    for j in range(m):
        t=int(input())
        col.append(t)
    arr.append(col)
sum=0
for i in range(n):
    for j in range(m):
        if(j==0):
            sum=sum+arr[i][j]
print(sum)
            
    