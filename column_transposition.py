def columnar_encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    rows = -(-len(text)//cols)
    text = text.ljust(rows*cols, "X")

    matrix = [text[i*cols:(i+1)*cols] for i in range(rows)]
    order = sorted(range(cols), key=lambda x: key[x])

    cipher = ""
    for c in order:
        for r in range(rows):
            cipher += matrix[r][c]
    return cipher

plaintext = "HELLO WORLD"
key = "ZEBRA"
print(columnar_encrypt(plaintext, key))
