s = input()
result = ""

for i in range(len(s)):
    if s[i] == " ":
        result += " "
    elif s.count(s[i]) > 1:
        if s[i] not in result:
            result += s[i]

if result.strip() == "":
    print("None")
else:
    print(result)
