import math
def encryptMessage(msg):
    col = len(key)
    row = math.ceil(len(msg) / col)
    padding = '_' * ((row * col) - len(msg))
    msg += padding
    matrix = [msg[i:i + col] for i in range(0, len(msg), col)]
    key_order = sorted(list(key))
    cipher = ''
    for char in key_order:
        col_idx = key.index(char)
        cipher += ''.join(row[col_idx] for row in matrix)
    return cipher
def decryptMessage(cipher):
    col = len(key)
    row = math.ceil(len(cipher) / col)
    key_order = sorted(list(key))
    matrix = [[None] * col for _ in range(row)]
    idx = 0
    for char in key_order:
        col_idx = key.index(char)
        for r in range(row):
            matrix[r][col_idx] = cipher[idx]
            idx += 1
    msg = ''.join(char for row in matrix for char in row )
    return msg.rstrip('_')
msg=input("Enter plain text:")
key=input("Enter key with distinct characters:") 
cipher = encryptMessage(msg)
print("Encrypted Message:", cipher)
print("Decrypted Message:", decryptMessage(cipher))
