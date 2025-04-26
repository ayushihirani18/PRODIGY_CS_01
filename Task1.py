def encrypt(text, shift):

    result = ""
    for l in text:
        
        if (l.isupper()):
            result += chr((ord(l) + shift - 65) % 26 + 65)

        elif (l.islower()):
            result += chr((ord(l) + shift - 97) % 26 + 97)

        else:
            result+= l
    return result

text = input("Enter the text to encrypt:")
shift = int(input("Enter the shift key (1-25):"))
cipher = print(f"Encrypted text :" + encrypt(text,shift))
