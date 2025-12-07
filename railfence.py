def rail_fence_encrypt(text, key):
    rails = [""] * key
    row, step = 0, 1
    for ch in text:
        rails[row] += ch
        if row == 0: step = 1
        elif row == key - 1: step = -1
        row += step
    return "".join(rails)
def rail_fence_decrypt(cipher, key):
    # Length of each rail
    pattern, row, step = [0]*len(cipher), 0, 1
    for i in range(len(cipher)):
        pattern[i] = row
        if row == 0: step = 1
        elif row == key-1: step = -1
        row += step
    rail_lengths = [pattern.count(r) for r in range(key)]
    # Split cipher into rails
    rails, idx = [], 0
    for ln in rail_lengths:
        rails.append(list(cipher[idx:idx+ln]))
        idx += ln
    # Rebuild text
    result, row, step = [], 0, 1
    for i in range(len(cipher)):
        result.append(rails[row].pop(0))
        if row == 0: step = 1
        elif row == key-1: step = -1
        row += step
    return "".join(result)
# Example
plaintext = "HELLO WORLD"
key = 3
cipher = rail_fence_encrypt(plaintext, key)
print("Rail Fence Encrypted:", cipher)
print("Rail Fence Decrypted:", rail_fence_decrypt(cipher, key))
