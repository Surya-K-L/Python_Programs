# Write a program to read 2 strings and see if they are equal (ignore case). 

# Should not use any built in functions. A function should be written.

# For example:

# Input	Result
# Hello   Yes
# hello

# Hai     No
# Bye

n=input().lower()
m=input().lower()
c=0
if len(n)!=len(m):
    print("No")
else:
    for i in range(len(n)):
        if(n[i]==m[i]):
            continue
        else:
            c=1
            print("No")
            break
if(c==0):
    print("Yes")