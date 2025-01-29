# Write a program to store characters in an array and display them.

# For example:

# Input	Result
# 5       ABCDE
# A
# B
# C
# D
# E

# 10      SRISHAKTHI
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
    cha.append(t)
for i in range(n):
    print(cha[i],end="")