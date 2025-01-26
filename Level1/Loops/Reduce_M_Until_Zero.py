# For the given number N,reduce M until it reaches zero & display the sequence of numbers.

# For example:

# Input	Result
# 7       7 4 1
# 3

# 6       6 4 2 0
# 2


n=int(input())
m=int(input())
for x in range(n,-1,-m):
    print(x,end=" ")