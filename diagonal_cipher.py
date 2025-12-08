def diagonal_encrypt(text, cols):
    text = text.replace(" ", "")
    rows = -(-len(text)//cols)
    text = text.ljust(rows * cols, "X")

    matrix = [list(text[i*cols:(i+1)*cols]) for i in range(rows)]
    cipher = ""

    r = 0
    c = 0
    for _ in range(rows * cols):
        cipher += matrix[r][c]
        r = (r + 1) % rows
        c = (c + 1) % cols

    return cipher

plaintext = "HELLO WORLD"
print(diagonal_encrypt(plaintext, 4))
