s = input()
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)
