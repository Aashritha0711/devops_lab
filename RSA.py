import math
p, q = map(int, input('Enter the primes p and q: ').split())
n = p * q
phi = (p - 1) * (q - 1)
for i in range(2, phi):
    if math.gcd(i, phi) == 1:
        e = i
        break
d = pow(e, -1, phi)
m = int(input("Enter the message (must be < n): "))
if m >= n:
    print("Message must be smaller than n.")
    exit()
ct = pow(m, e, n)
print("Public key:", (e, n))
print("Private key:", (d, n))
print("Encrypted message:", ct)
print("Decrypted message:", pow(ct, d, n))
