n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = [0] * n
b[0]=a[0]
for i in range(1, n, 2):
    if i + 1 < n:  
        b[i] = a[i + 1]
        b[i + 1] = a[i]
    else:
        b[i] = a[i]  
print(b)
