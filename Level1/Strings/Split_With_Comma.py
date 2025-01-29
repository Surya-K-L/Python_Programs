# Read and display a set of strings given separated by commas

# For example:

# Input	                        Result
# Trial, Boys, Car, Now, This     Trial
#                                 Boys
#                                 Car
#                                 Now
#                                 This
                                
# Street, Show, This              Street
#                                 Show
#                                 This


n=list(map(str,input().split(", ")))
for x in n:
    print(x)