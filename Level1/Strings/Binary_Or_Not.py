# Write a program to check whether a string is binary string or not.

# Input Format

# 10111

# Constraints

# Length of the string should be greater than 1 or less than 100.

# Output Format

# True


n=input()
l=len(n)
r=0
for i in range(l):
    if(n[i]=='0' or n[i]=='1'):
        continue
    else:
        r=1
        print("False")
        break
if(r==0):
    print("True")
