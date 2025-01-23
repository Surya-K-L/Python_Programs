# Check if the middle number of a given 3 digit number is divisible by 5

# Note: Consider the count of digits in the number be odd.

# For example:

# Input	Result
# 353     Yes
# 372     No


n=int(input())
t=n/10
p=int(t%10)
if p%5==0:
    print("Yes")
else:
    print("No")