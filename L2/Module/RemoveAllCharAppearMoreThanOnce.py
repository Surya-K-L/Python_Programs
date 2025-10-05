s = input()
result = ""
for ch in s:
    if s.count(ch)==1:
        result+=ch
print(result)
