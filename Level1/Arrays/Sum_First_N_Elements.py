# Write the program to sum the first N elements in the array

# 5  <- Total number of elements in the array
# 11 20 30 40 50 <- Array elements
# 2 <- Number of elements to add (index 0 and index 1)

# Output:
# 31

# For example:

# Input	        Result
# 5               33
# 10 20 3 4 5
# 3

# 3               3
# 1 2 3
# 2


n=int(input())
arr=list(map(int,input().split()))
k=int(input())
t=0
for i in range(k):
    t=t+arr[i]
print(t)
