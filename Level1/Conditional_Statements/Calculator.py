# Write a program to design a calculator with basic operations(+,_,*,/,%)

# For example:

# Input	Result
# +       11
# 5
# 6

# %       1
# 9
# 4

c=input()
n1=int(input())
n2=int(input())
if c=='+':
    print(n1+n2)
elif c=='-':
    print(n1-n2)
elif c=='*':
    print(n1*n2)
elif c=='/':
    print(int(n1/n2))
elif c=='%':
    print(n1%n2)

