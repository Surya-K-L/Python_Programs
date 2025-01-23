# A library charges a fine for every book returned late. For the first 5 days, the fine is 50 paise, for

# 6-10 days fine is one rupee and for above 10 days the fine is 5 rupees. If you return the book

# after 30 days, message should be "Membership Cancelled". Write a program to accept the number of days

# the member is late to return the book and display the fine or the appropriate member cancellation

# message.


# For example:

# Input	Result
# 7       Fine is 1 rupee
# 4       Fine is 50 paise
# 40      Membership Cancelled
# 12      Fine is 5 rupees


days=int(input())
if(days>=1 and days<=5):
    print("Fine is 50 paise")
elif(days>=6 and days<=10):
    print("Fine is 1 rupee")
elif(days>5 and days<30):
    print("Fine is 5 rupees")
else:
    print("Membership Cancelled")