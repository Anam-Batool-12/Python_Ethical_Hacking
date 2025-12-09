def diagonal_zigzag_encrypt(text, cols):
    text = text.replace(" ", "")
    rows = -(-len(text)//cols)
    text = text.ljust(rows * cols, "X")

    matrix = [list(text[i*cols:(i+1)*cols]) for i in range(rows)]
    cipher = ""

    r = 0
    c = 0
    direction = 1

    for _ in range(rows * cols):
        cipher += matrix[r][c]

        if direction == 1:
            if r == rows - 1:
                c += 1
                direction = -1
            else:
                r += 1
                c += 1
        else:
            if r == 0:
                c += 1
                direction = 1
            else:
                r -= 1
                c += 1

        if c >= cols:
            c = c % cols

    return cipher

plaintext = "HELLO WORLD"
print(diagonal_zigzag_encrypt(plaintext, 4))
