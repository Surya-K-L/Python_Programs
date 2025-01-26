# Write a Program to read a number from user and print it in words.
# For example:

# Input	Result
# 4372    Four Three Seven Two
# 504     Five Zero Four


n=int(input())
t=0
while(n>0):
    p=n%10
    t=t*10+p
    n=int(n/10)
k=0
while(t>0):
    z=t%10
    t=int(t/10)
    if(z==0):
        print("Zero",end=" ")
    elif(z==1):
        print("One",end=" ")
    elif z==2:
        print("Two",end=" ")
    elif z==3:
        print("Three",end=" ")
    elif z==4:
        print("Four",end=" ")
    elif z==5:
        print("Five",end=" ")
    elif z==6:
        print("Six",end=" ")
    elif z==7:
        print("Seven",end=" ")
    elif z==8:
        print("Eight",end=" ")
    elif z==9:
        print("Nine",end=" ")