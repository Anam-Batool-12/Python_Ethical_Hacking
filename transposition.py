def transposition_encrypt(message, key):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)

message = input("Enter your message: ")
key = int(input("Enter your key (number): "))

encrypted = transposition_encrypt(message, key)
print("Encrypted message:", encrypted)
