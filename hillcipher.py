import numpy as np
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    return None
def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += "X"
    cipher = ""
    for i in range(0, len(plaintext), 2):
        pair = [ord(plaintext[i])-65, ord(plaintext[i+1])-65]
        result = np.dot(key_matrix, pair) % 26
        cipher += chr(result[0]+65) + chr(result[1]+65)
    return cipher
def hill_decrypt(cipher, key_matrix):
    det = int(round(np.linalg.det(key_matrix)))
    inv_det = mod_inverse(det, 26)
    if inv_det is None:
        raise ValueError("Key matrix is not invertible")
    adj = np.round(det * np.linalg.inv(key_matrix)) % 26
    inv_matrix = (inv_det * adj) % 26
    plaintext = ""
    for i in range(0, len(cipher), 2):
        pair = [ord(cipher[i])-65, ord(cipher[i+1])-65]
        result = np.dot(inv_matrix, pair) % 26
        plaintext += chr((result[0])+65) + chr((result[1])+65)
    return plaintext

key_matrix = np.array([[3, 3], [2, 5]])
plaintext = "HELLO"
cipher = hill_encrypt(plaintext, key_matrix)
print("Hill Encrypted:", cipher)
print("Hill Decrypted:", hill_decrypt(cipher, key_matrix))
