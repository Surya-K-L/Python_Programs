# Print the maximum of n given numbers. 

# NOTE: You should not declare an array

# For example:

# Input	  Result
# 5       30
# 10
# 20
# 30
# 15
# 5

n=int(input())
max=0
for x in range(0,n):
    t=int(input())
    if max<t:
        max=t
print(max)

