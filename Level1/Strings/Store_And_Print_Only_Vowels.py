# Write a program to store characters in an array and print only the vowels only

# For example:

# Input	Result
# 5       AE
# A
# B
# C
# D
# E

# 10      IAI
# S
# R
# I
# S
# H
# A
# K
# T
# H
# I


n=int(input())
cha=[]
for i in range(n):
    t=input()
    if(t=="A" or t=="E" or t=="I" or t=="O" or t=="U"):
        cha.append(t)
for i in cha:
    print(i,end="")
