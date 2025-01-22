# Write  a prohram to Check if the given number is between 17 and 33 (both inclusive)
# For example:

# Input	Result
# 17      boundary
# 22      YES
# 50      NO


n=int(input())
if n==17 or n==33:
    print("boundary")
elif n>=17 and n<=33:
    print("YES")
else:
    print("NO")