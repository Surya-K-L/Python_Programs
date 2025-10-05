s1 = input()  
s2 = input() 

result = ""
i = 0
len_s2 = len(s2)

while i < len(s1):
    if s1[i:i+len_s2] == s2:
        result += s1[i:i+len_s2].upper()
        i += len_s2
    else:
        result += s1[i]
        i += 1
print(result)
