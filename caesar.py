def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

# Example
plaintext = "HELLO WORLD"
shift = 3
cipher = caesar_encrypt(plaintext, shift)
print("Caesar Encrypted:", cipher)
print("Caesar Decrypted:", caesar_decrypt(cipher, shift))
