# Write a program to read a number (0-6) and print the weekday name.

# Sample Input1: 5

# Sample Output1: Friday

# Sample Input2 :9

# Sample Output2: Invalid weekday

# For example:

# Input	Result
# 0       Sunday
# 3       Wednesday
# 9       Invalid weekday

a=int(input())
if(a==0):
    print("Sunday")
elif a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
else:
    print("Invalid weekday")