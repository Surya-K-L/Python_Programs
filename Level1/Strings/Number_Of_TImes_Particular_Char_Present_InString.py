# Find the number of times a character is present in the string

# For example:

# Input	Result
# Hello   2
# l

# Trait   1  
# t

# Belong  0
# k

n=input()
k=input()
c=0
for x in range(len(n)):
     if(n[x]==k):
        c=c+1
print(c)