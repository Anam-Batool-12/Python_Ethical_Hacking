message = input("Enter the encrypted message: ")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
output = ""

print("=== Brute Force Results ===")

for key in range(26):
    result = ""

    for char in message:
        if char.isalpha():
            # Uppercase
            if char.isupper():
                shifted = (ord(char) - ord('A') - key) % 26
                result += chr(shifted + ord('A'))
            # Lowercase
            else:
                shifted = (ord(char) - ord('a') - key) % 26
                result += chr(shifted + ord('a'))
        else:
            result += char

    print(f"Key {key}: {result}")
