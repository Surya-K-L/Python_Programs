# Trendy Numbers

# A number is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by 3.

# Examples of Trendy Numbers: 131, 264, 999

# Examples of NonTrendy Numbers : 123, 653, 33, 4, 1034

# Write a program to find whether a given number is a Trendy Number or not.


# For example:

# Input	Result
# 235     Trendy Number
# 123     Not a Trendy Number


n=int(input())
if(n>99 and n<1000):
    l=int(n/10)
    m=l%10
    print("Trendy Number") if(m%3==0) else print("Not a Trendy Number")
else:
    print("Not a Trendy Number")