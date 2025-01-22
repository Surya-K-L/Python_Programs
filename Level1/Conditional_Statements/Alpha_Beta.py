# A character and number are given as input

# If the number is between 1 to 10 and character is between A to C then print ALPHA

# If the number is between 11 to 30 and character is between D to R then print BETA

# If the number is between 1 to 10 and character is between D to R then print GAMMA

# If the number is between 11 to 30 and character is between A to C then print DELTA

# Otherwise print OMEGA

# For example:

# Input	Result
# A       ALPHA
# 3

# R       BETA
# 30

# R       GAMMA
# 10

# C       DELTA
# 11

# Z       OMEGA
# 100

# X       OMEGA
# 7

c=input()
n=int(input())
if((n>=1 and n<=10) and (c>='A' and c<='C')):
    print("ALPHA")
elif ((n>=11 and n<=30) and (c>='D' and c<='R')):
    print("BETA")
elif ((n>=1 and n<=10) and (c>='D' and c<='R')):
    print("GAMMA")
elif ((n>=11 and n<=30) and (c>='A' and c<='C')):
    print("DELTA")
else:
    print("OMEGA")

