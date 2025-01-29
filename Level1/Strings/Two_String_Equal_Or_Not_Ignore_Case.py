# Program to compare if two strings are equal or not .ignoring the case

# Input:

# The first line of input is the integer T, denoting number of test cases. The first line of each test case is two input strings S1, S2 on the same line separated by a single space respectively.

# Output:

# For each test case, there is one line of output i.e. whether the Strings are equal or Strings are not equal

# Input    :
# 3
# codevita codevita
# Hackerrank Hackerearth
# Codevita codeVita

# Output :
# Strings are equal
# Strings are not equal
# Strings are equal



n=int(input())
for i in range(n):
    str1,str2=map(str,input().split(" "))
    if(str1.lower()==str2.lower()):
        print("Strings are equal")
    else:
        print("Strings are not equal")