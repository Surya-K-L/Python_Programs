n, m, k = map(int, input().split())
a = list(map(int, input().split())) 
b = list(map(int, input().split()))  
a.sort()
b.sort()

i = 0  
j = 0
count = 0 
while i < n and j < m:
    if abs(a[i] - b[j]) <= k:
        count += 1
        i += 1
        j += 1
    elif b[j] < a[i] - k:
        j += 1
    else:
        i += 1
print(count)
