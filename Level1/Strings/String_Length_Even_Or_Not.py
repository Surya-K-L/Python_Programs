# Find if a given string has even number of characters or odd number of characters

# For example:

# Input	Result
# hello   odd
# good    even


n=input()
l=len(n)
print("even") if l%2==0 else print("odd")