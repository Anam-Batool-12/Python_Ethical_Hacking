message = input("Select options.\nEncrypt \nDecrypt: ")

if message == "Encrypt":
    print("Encrypting your message....")
    message = input("Enter your message: ")

    translated = ""
    i = len(message) - 1

    while i >= 0:
        translated = translated + message[i]
        i = i - 1

    print("Encrypted Message:", translated)

elif message == "Decrypt":
    print("Decrypting your message....")
    message2 = input("Enter your message: ")

    translated = ""
    i = len(message2) - 1

    while i >= 0:
        translated = translated + message2[i]
        i = i - 1

    print("Decrypted Message:", translated)

else:
    print("Invalid option.")
