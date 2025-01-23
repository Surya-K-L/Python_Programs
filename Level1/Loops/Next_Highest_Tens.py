# Find the next highest tens number

# For example:

# Input	Result
# 7       10
# 33      40
# 99      100


n=int(input())
t=n%10
k=10-t
print(n+k)