# Write a program to read two numbers from user and perform bitwise operations like Bitwise AND, Bitwise OR, Bitwise EXOR, Left Shift and Right Shift.

# For example:

# Input	Result
# 10 3    iNum1 & iNum2 is 2
#         iNum1 | iNum2 is 11
#         iNum1 ^ iNum2 is 9
#         iNum1 << iNum2 is 80
#         iNum1 >> iNum2 is 1

# 4 2     iNum1 & iNum2 is 0
#         iNum1 | iNum2 is 6
#         iNum1 ^ iNum2 is 6
#         iNum1 << iNum2 is 16
#         iNum1 >> iNum2 is 1

num1,num2=map(int,input().split())
print(f"iNum1 & iNum2 is {num1&num2}")
print(f"iNum1 | iNum2 is {num1|num2}")
print(f"iNum1 ^ iNum2 is {num1^num2}")
print(f"iNum1 << iNum2 is {num1<<num2}")
print(f"iNum1 >> iNum2 is {num1>>num2}")

