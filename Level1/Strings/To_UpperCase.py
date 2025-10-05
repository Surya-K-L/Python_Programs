n=int(input())
for i in range(n):
    ch=input()[0]
    if 'a'<=ch <='z':
        print(chr(ord(ch)-32),end="")
    else:
        print(ch,end="")
