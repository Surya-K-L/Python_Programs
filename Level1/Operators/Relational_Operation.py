# Write a program to read two numbers from user and perform relational operations like >, <, >=, <=, ==, !=.


# For example:

# Input	Result

# 5       iNum1 == iNum2 is false
# 8       iNum1 != iNum2 is true
#         iNum1 >= iNum2 is false
#         iNum1 <= iNum2 is true
#         iNum1 > iNum2 is false
#         iNum1 < iNum2 is true

# 12      iNum1 == iNum2 is true
# 12      iNum1 != iNum2 is false
#         iNum1 >= iNum2 is true
#         iNum1 <= iNum2 is true
#         iNum1 > iNum2 is false
#         iNum1 < iNum2 is false


num1=int(input())
num2=int(input())
print(f"iNum1 == iNum2 is {'true' if num1==num2 else 'false'}")
print(f"iNum1 != iNum2 is {'true' if num1!=num2 else 'false'}")
print(f"iNum1 >= iNum2 is {'true' if num1>=num2 else 'false'}")
print(f"iNum1 <= iNum2 is {'true' if num1<=num2 else 'false'}")
print(f"iNum1 > iNum2 is {'true' if num1>num2 else 'false'}")
print(f"iNum1 < iNum2 is {'true' if num1<num2 else 'false'}")
