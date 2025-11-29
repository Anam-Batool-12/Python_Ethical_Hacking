# Stored credentials
correct_username = "admin"
correct_password = "secret123"

# Max login attempts
attempts = 3

print("=== Login System ===")

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome.")
        break
    else:
        attempts -= 1
        print("Incorrect username or password.")
        print("Attempts left:", attempts)
        print()

if attempts == 0:
    print("Account locked due to too many failed attempts.")
