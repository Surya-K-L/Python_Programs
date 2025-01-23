# Write a program to find the factorial of a given number.

# Example

# sample input1: 5

# sample output1: 120

# sample input2: 4

# sample output2: 24


n=int(input())
f=1
while(n>0):
    f=f*n
    n=n-1
print(f)