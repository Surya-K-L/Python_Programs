n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
t = n - 1
for i in range(n // 2):
    print(a[i])
    print(a[t])
    t -= 1
if n % 2 == 1:
    print(a[n // 2])
