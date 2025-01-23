# Write a program to print all natural numbers from 1 to n.

# Sample Input

# 10

# Sample Output

# Natural numbers from 1 to 10: 1 2 3 4 5 6 7 8 9 10

# For example:

# Input	Result
# 5     Natural numbers from 1 to 5: 1 2 3 4 5



n=int(input())
print(f"Natural numbers from 1 to {n}:",end=" ")
for x in range(1,n+1):
    print(x,end=" ")