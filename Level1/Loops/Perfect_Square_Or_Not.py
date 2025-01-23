# Check whether the given number is perfect square or not.
# Hint: Use Square Root function

# For example:

# Input	Result
# 121
# Perfect square number
# 236
# Not a perfect square number


import math
n=int(input())
t=int(math.sqrt(n))
if(t*t==n):
    print("Perfect square number")
else:
    print("Not a perfect square number")