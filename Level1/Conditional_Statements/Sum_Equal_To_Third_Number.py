# Write a program to check if the addition of the first 2 numbers results in the 3rd number

# For example:

# Input	Result
# 2       TRUE
# 1
# 3

# 10      TRUE
# 20
# 30

# 10      FALSE
# 20
# 10

a=int(input())
b=int(input())
c=int(input())
if a+b==c:
    print("TRUE")
else:
    print("FALSE")
