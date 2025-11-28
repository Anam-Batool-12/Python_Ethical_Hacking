message = input("Encrypt or Decrypt: ")

if message == "Encrypt":
    text = input("Enter your message: ")
    key = int(input("Enter numeric key: "))
    result = ""

    for char in text:
        if char.isalpha():
            shift = ord(char) + key
            if char.islower():
                if shift > ord('z'):
                    shift -= 26
            else:
                if shift > ord('Z'):
                    shift -= 26
            result += chr(shift)
        else:
            result += char

    print("Encrypted:", result)

elif message == "Decrypt":
    text = input("Enter your message: ")
    key = int(input("Enter numeric key: "))
    result = ""

    for char in text:
        if char.isalpha():
            shift = ord(char) - key
            if char.islower():
                if shift < ord('a'):
                    shift += 26
            else:
                if shift < ord('A'):
                    shift += 26
            result += chr(shift)
        else:
            result += char

    print("Decrypted:", result)
