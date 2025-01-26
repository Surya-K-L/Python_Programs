# A Kaprekar number is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 452 = 2025 and 20+25 = 45. Write a Program to find given number is Kaprekar number ot not.

# For example:

# Input	Result
# 45      Kaprekar Number
# 13      Not a Kaprekar Number


n=int(input())
sq=n*n
le=len(str(abs(sq)))
if(le%2==0):
    fir=int(sq/100)
    sec=sq%100
    t=fir+sec
    if(t==n):
        print("Kaprekar Number")
    else:
        print("Not a Kaprekar Number")
else:
    print("Not a Kaprekar Number")