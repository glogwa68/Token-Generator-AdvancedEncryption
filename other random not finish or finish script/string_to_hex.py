def binary_to_text(code):
    a = ''
    for i in range(0, len(code), 8):
        a += chr(int(code[i:i+8], 2))
    return a


def text_to_binary(text):
    return ' '.join(format(ord(x), 'b') for x in text)

if __name__ == '__main__':
    print("1. Convert text into binary code")
    print("2. Convert binary code to text")
    print("Type 1 or 2.")
    ch = input("Choose: ")
    if ch == "1":
        ip = input("Enter your string: ")
        print("Result: " + str(text_to_binary(ip)))
    elif ch == "2":
        ip2 = input("Enter your binary string: ")
        print("Result: " + str(binary_to_text(ip2)))
    else:
        print("Not a valid option")
        quit()