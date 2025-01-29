# Write a program to hop one letter and print the string as given in the example below

# For example:

# Input	    Result
# string      srn
# println     pitn


str=input()
l=len(str)
for i in range(0,l,2):
    print(str[i],end="")