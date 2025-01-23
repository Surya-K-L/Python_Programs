# Write a Program read a number and perform the following,

# If it is divisible by 3 and 5, Print "FooBar" 
# If it is divisible by 3, Print "Foo"
# If it is divisible by 5, Print "Bar"  and 
# If it is not divisible by 3 and 5, Print "None".
# Sample Input
# 4
# 21
# 25
# 30
# 11

# Sample Output
# Foo
# Bar
# FooBar
# None

# Input Format

# The first line of input is the integer T, denoting a number of test cases. The first line of each test case is an integer N

# Constraints

# 1<=T<=100 0<=N<=1000

# Output Format

# For each test case, there is one line of output i.e. Foo or Bar or FooBar or None.


n=int(input())
while(n>0):
    num=int(input())
    n=n-1
    if (num % 3 == 0 and num % 5 == 0):
        print("FooBar")
    elif(num % 3 == 0):
        print("Foo")
    elif(num % 5 == 0):
        print("Bar")
    else:
        print("None")