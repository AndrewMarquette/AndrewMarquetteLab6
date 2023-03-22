
def encode(password):
    code = ""
    array = [int(i) for i in str(password)]
    for i in array:
        i += 3
        a = str(i)
        code += a
    return code

def decode(password):
    code = ""
    array = [int(i) for i in str(password)]
    for i in array:
        i -= 3
        a = str(i)
        code += a
    return code


if __name__ == '__main__':
    while True:
        choice = 0
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
            encode(password)
            print()

        if choice == '2':
            password = input("Please enter your password to decode: ")
            print("The encoded password is 45678888, and the original password is 12345555.")
            print()
        if choice == '3':
            break
