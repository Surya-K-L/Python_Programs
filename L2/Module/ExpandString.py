s = input()
result = ""
i = 0
while i < len(s):
    char = s[i]
    i += 1
    num = ""
    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    if num:  
        result += char * int(num)
    else:  
        result += char

print(result)
