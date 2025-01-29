# Reverse every word in a given sentence

# For example:

# Input	        Result
# This is it      sihT si ti


n=input()
str=n.split(" ")
for x in str:
    p=x[::-1]
    print(p,end=" ")