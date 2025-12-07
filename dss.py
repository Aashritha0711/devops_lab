import random
def mod_inverse(a, m):
    return pow(a, -1, m)
def hash_message(msg, q):
    return sum((ord(c) * (i + 1) for i, c in enumerate(msg))) % q                                                                                                                 
def dss_sign(message, p, q, g, private_key):
    h = hash_message(message, q)
    while True:
        k = random.randint(1, q - 1)
        r = pow(g, k, p) % q
        if r == 0:
            continue
        k_inv = mod_inverse(k, q)
        s = (k_inv * (h + private_key * r)) % q
        if s == 0:
            continue
        return s, r
def dss_verify(message, s, r, p, q, g, public_key):
    if not (0 < r < q and 0 < s < q):
        return False
    h = hash_message(message, q)
    w = mod_inverse(s, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(public_key, u2, p) % p) % q
    return v == r
if __name__ == "__main__":
    q = 11  
    p = 23  
    g = 4   
    private_key = 6  
    public_key = pow(g, private_key, p)  
    message = "network"
    s, r = dss_sign(message, p, q, g, private_key)
    print(f"Message: {message}")
    print(f"Signature (s, r): ({s}, {r})")

    valid = dss_verify(message, s, r, p, q, g, public_key)
    if valid:
        print("Signature is VERIFIED for the original message.")
    else:
        print("Signature is NOT VERIFIED for the original message.")

    tampered = "worknet"
    print(f"Tampered Message:{tampered}")
    valid_tampered = dss_verify(tampered, s, r, p, q, g, public_key)
    if valid_tampered:
        print("Signature is VERIFIED for the tampered message. (Error!)")
    else:
        print("Signature is NOT VERIFIED for the tampered message.")
