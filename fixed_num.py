def transpose_encrypt(text, columns):
    text = text.replace(" ", "")
    rows = -(-len(text) // columns)
    matrix = []

    index = 0
    for _ in range(rows):
        row = text[index:index+columns]
        matrix.append(row.ljust(columns, 'X'))
        index += columns

    cipher = ""
    for c in range(columns):
        for r in range(rows):
            cipher += matrix[r][c]

    return cipher

plaintext = "HELLO WORLD"
cipher = transpose_encrypt(plaintext, 4)
print(cipher)
