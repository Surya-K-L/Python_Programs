# Write a program to get integer input from the user and print "FooBar" if the number is divisible by 3 & 5 and print "Foo" if the number is divisible by 3 and print "Bar" if the number is divisible by 5 and print "None" if the number is not divisible by 3 and 5.

# For example:

# Input	Result
# 15      FooBar
# 25      Bar

num=int(input())
if(num%3==0  and num%5==0):
    print("FooBar")
elif(num%3==0):
    print("Foo")
elif(num%5==0):
    print("Bar")
else:
    print("None")
