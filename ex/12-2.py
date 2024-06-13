def strength(password):
    result = {}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True

    for i in password:
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["uppercase"] = uppercase

    if all(result.values()):
        return ("Strong Password")
    else:
        return ("Weak password")


password = input("Enter new password: ")
print(strength(password))
