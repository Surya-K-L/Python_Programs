# Write a program to receive a character as user input and determine if that character is upper case letter (capital letter) or lower case letter (small letter) or a number (0-9) or some other character.

# Hint: Refer to the ASCII table.

# For example:

# Input	Result
# g       Lower case letter
# H       Upper case letter
# !       Special character
# 8       Number


c=input()[0]
ch=ord(c)
if(ch>=65 and ch<=90):
    print("Upper case letter")        
elif (ch>=97 and ch<=122):
    print("Lower case letter") 
elif (ch>=48 and ch<=57):
    print("Number")
else:
    print("Special character")
    