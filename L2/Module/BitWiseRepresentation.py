n=int(input())
lsb=(n&-n).bit_length()-1
msb=n.bit_length()-1
bic=bin(n).count('1')
s=""
s=str(bic)+"#"+str(lsb)+"#"+str(msb)
print(s)
