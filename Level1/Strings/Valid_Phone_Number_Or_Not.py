# Find the given phone number is valid or not. 

# Note: A valid phone number will have 10 numeric digits 

# Input 1:  9876543210 

# Output 1: Valid Mobile number 

# Input 2: IONIXX12345 

# Output 2: 

# Invalid mobile number 

# Input 3: 923452342 

# Output 3: 

# Invalid mobile number 


# For example:

# Input	        Result
# srishakthi123   Invalid mobile number 

n=input()
if(len(n)!=10):
    print("Invalid mobile number")
else: 
    if n.isdigit():
        print("Valid Mobile number")
    else:
        print("Invalid mobile number")
