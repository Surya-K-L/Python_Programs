# Find the next highest 10s number

# For example:

# Input	Result
# 33      40
# 55      60
# 99      100

num=int(input())
t=num%10
next=10-t
print(num+next)
