# Compress the given strings as given below
# INPUT
# aaabbb
# OUTPUT
# a3b3

# INPUT
# ab
# OUTPUT
# a1b1


# For example:

# Input	Result
# aaabbb  a3b3
# abc     a1b1c1


str=input()
l=len(str)
c=0
i=0
while(i<l):
    c=1
    while(i<l-1 and str[i]==str[i+1]):
        c=c+1
        i=i+1
    print(str[i],end="")
    print(c,end="")
    i+=1
    