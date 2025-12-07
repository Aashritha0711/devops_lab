def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix, used = [], set()
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c.isalpha() and c not in used:
            matrix.append(c); used.add(c)
    return [matrix[i:i+5] for i in range(0, 25, 5)]
def find_position(matrix, ch):
    for i in range(len(matrix)):
        row = matrix[i]
        if ch in row:
            return i, row.index(ch)
def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = text.upper().replace('J','I')
    pairs, i = [], 0
    while i < len(text):
        a, b = text[i], text[i+1] if i+1 < len(text) else "X"
        if a == b: pairs.append((a,"X")); i += 1
        else: pairs.append((a,b)); i += 2
    result = ""
    for a, b in pairs:
        r1,c1 = find_position(matrix,a); r2,c2 = find_position(matrix,b)
        if r1==r2: result += matrix[r1][(c1+1)%5]+matrix[r2][(c2+1)%5]
        elif c1==c2: result += matrix[(r1+1)%5][c1]+matrix[(r2+1)%5][c2]
        else: result += matrix[r1][c2]+matrix[r2][c1]
    return result
def playfair_decrypt(cipher, key):
    matrix = generate_key_matrix(key)
    result = ""
    for i in range(0, len(cipher), 2):
        a,b = cipher[i], cipher[i+1]
        r1,c1 = find_position(matrix,a); r2,c2 = find_position(matrix,b)
        if r1==r2: result += matrix[r1][(c1-1)%5]+matrix[r2][(c2-1)%5]
        elif c1==c2: result += matrix[(r1-1)%5][c1]+matrix[(r2-1)%5][c2]
        else: result += matrix[r1][c2]+matrix[r2][c1]
    cleaned = ""
    for i in range(len(result)):   
        ch = result[i]
        if not (ch=="X" and i>0 and i<len(result)-1 and result[i-1]==result[i+1]):
            cleaned += ch
    if cleaned.endswith("X"):
        cleaned = cleaned[:-1]
    return cleaned
key = "PLAYFAIR"
plaintext = "AASH"
cipher = playfair_encrypt(plaintext, key)
print("Encrypted:", cipher)
print("Decrypted:", playfair_decrypt(cipher, key))
