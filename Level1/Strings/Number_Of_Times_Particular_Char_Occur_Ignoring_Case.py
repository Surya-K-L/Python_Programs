# Count the number of times a particular character occurs ignoring case

# For example:

# Input	    Result
# Trait       2
# t

# pluSS       2
# s

# Braillie    0  
# k

n=input().lower()
m=input().lower()
c=0
for i in  range(len(n)):
    if(n[i]==m):
        c=c+1
print(c)
