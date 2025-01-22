# An angle is complementary if it is 90'

# An angle is supplementary if it is 180'

# An angle is complete if it is 0 or 360'

# Find if a given angle is one of the above, otherwise enter NONE

# For example:

# Input	    Result
# 90          COMPLEMENTARY
# 180         SUPPLEMENTARY
# 360         COMPLETE
# 0           COMPLETE
# 142         NONE


a=int(input())
if a==90:
    print("COMPLEMENTARY")
elif a==180:
    print("SUPPLEMENTARY")
elif a==360:
    print("COMPLETE")
elif a==0:
    print("COMPLETE")
else:
    print("NONE")