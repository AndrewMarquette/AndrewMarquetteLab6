# Andrew Marquette

def encode(password):
    code = ""
    array = [int(i) for i in str(password)]
    for i in array:
        i += 3
        a = str(i)
        code += a
    return code

def decode(code):
    decoded_password = ""
    for value in code:
        new_digit = str((int(value) - 3) % 10)
        decoded_password = decoded_password + new_digit

    return decoded_password

if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        choice = input("Please enter an option: ")
        if choice == '1':
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            code = encode(password)
            print()
        if choice == '2':
            original_password = decode(code)

            print(f"The encoded password is {code}, and the original password is {original_password} ")
        if choice == '3':
            break
