import pyperclip

simbletype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !?.'

message = input("Enter your message: ")
modetype = input("Type 'encrypt' or 'decrypt': ").lower()
keycode = int(input("Enter your numeric key: "))

encryption = ''

for symbol in message:
    if symbol in simbletype:
        symbolindex = simbletype.find(symbol)

        if modetype == 'encrypt':
            new_index = symbolindex + keycode

        elif modetype == 'decrypt':
            new_index = symbolindex - keycode

        if new_index >= len(simbletype):
            new_index = new_index % len(simbletype)
        elif new_index < 0:
            new_index = new_index % len(simbletype)

        encryption += simbletype[new_index]

    else:
        encryption += symbol
        
pyperclip.copy(encryption)
print("Output:", encryption)
print("The result has been copied to your clipboard.")
