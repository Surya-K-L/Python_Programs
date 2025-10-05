num = input()
digits = [int(d) for d in num]
digits = [(d + 5) % 10 for d in digits]
encrypted = f"{digits[2]}{digits[3]}{digits[0]}{digits[1]}"
print(encrypted)
