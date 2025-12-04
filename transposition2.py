def transposition_encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    rows = -(-len(text)//cols)  # ceiling division
    matrix = [text[i*cols:(i+1)*cols] for i in range(rows)]
    cipher = ''
    for k in sorted(range(len(key)), key=lambda x: key[x]):
        for row in matrix:
            if k < len(row):
                cipher += row[k]
    return cipher

plaintext = "HELLO WORLD"
key = [3, 1, 4, 2]
print(transposition_encrypt(plaintext, key))
