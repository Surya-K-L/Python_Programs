# Write a program to perform addition, subtraction, multiplication,  division and modulo operations.

# For example:

# Input	                Result
# 20 10                   iNum1 + iNum2 = 30
#                         iNum1 - iNum2 = 10
#                         iNum1 * iNum2 = 200
#                         iNum1 / iNum2 = 2
#                         iNum1 % iNum2 = 0
                        
# 45 89                   iNum1 + iNum2 = 134
#                         iNum1 - iNum2 = -44
#                         iNum1 * iNum2 = 4005
#                         iNum1 / iNum2 = 0
#                         iNum1 % iNum2 = 45


num1,num2=map(int,input().split())
print(f"iNum1 + iNum2 = {num1+num2}")
print(f"iNum1 - iNum2 = {num1-num2}")
print(f"iNum1 * iNum2 = {num1*num2}")
print(f"iNum1 / iNum2 = {num1//num2}")
print(f"iNum1 % iNum2 = {num1%num2}")
