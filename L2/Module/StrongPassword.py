passw = input()
z = 0
if len(passw) != 8:
    print("Your Password is Not Strong")
else:
    for c in passw:
        if (32 <= ord(c) <= 126):  
            z += 1
        if z == 1:  
            print("Your Password is Strong")
            break
