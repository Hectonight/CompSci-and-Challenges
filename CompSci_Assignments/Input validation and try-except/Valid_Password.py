import string


def has_letter(password):
    for char in password:
        if char in string.ascii_letters:
            return True
    return False


def has_number(password):
    for char in password:
        if char in string.digits:
            return True
    return False


while True:
    Password = input("Enter your new password. ")
    if len(Password) >= 7 and has_letter(Password) and has_number(Password):
        print("Correct!")
        break
    print("Invalid input")
