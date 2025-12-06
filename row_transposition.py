def row_reverse_encrypt(text, cols):
    text = text.replace(" ", "")
    rows = -(-len(text)//cols)
    matrix = [text[i*cols:(i+1)*cols] for i in range(rows)]
    cipher = ''
    for row in matrix:
        cipher += row[::-1]
    return cipher

plaintext = "HELLO WORLD"
cols = 4
print(row_reverse_encrypt(plaintext, cols))
