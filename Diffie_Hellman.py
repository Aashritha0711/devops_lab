import random
p = int(input("Enter prime number p:")) 
q = int(input("Enter primitive root q:"))
a = random.randint(2, p - 2)  
A = pow(q, a, p)              
print(f"\n[Alice] Private Key (a): {a}")
print(f"[Alice] Public Key (A): {A}")
b = random.randint(2, p - 1)  
B = pow(q, b, p)              
print(f"\n[Bob] Private Key (b): {b}")
print(f"[Bob] Public Key (B): {B}")
shared_secret_alice = pow(B, a, p)
shared_secret_bob = pow(A, b, p)
print(f"\n[Alice] Computed Shared Secret: {shared_secret_alice}")
print(f"[Bob] Computed Shared Secret:   {shared_secret_bob}")
if shared_secret_alice == shared_secret_bob:
    print("\n Shared secret successfully established!")
else:
    print("\n Shared secret mismatch! Something went wrong.")
