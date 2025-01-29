# Search for a substring within a string

# For example:

# Input	                    Result
# HelloWorld                  Starts at position 6
# World

# Friends are always there    Starts at position 13
# always


str1=input()
str2=input()
print("Starts at position",str1.rfind(str2)+1)