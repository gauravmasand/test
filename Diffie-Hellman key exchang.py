# Diffie-Hellman Key Exchange Implementation

def power_mod(base, exponent, mod):
    """Efficient modular exponentiation"""
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result = (result * base) % mod
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % mod
    return result

def diffie_hellman_key_exchange():
    # Step 1: Publicly known values
    P = 23  # Prime number
    G = 9   # Primitive root modulo P
    print(f"Publicly Shared Prime (P): {P}")
    print(f"Publicly Shared Base (G): {G}")

    # Step 2: Private keys
    a = 4  # Alice's private key
    b = 3  # Bob's private key
    print(f"\nAlice's Private Key (a): {a}")
    print(f"Bob's Private Key (b): {b}")

    # Step 3: Compute public keys
    x = power_mod(G, a, P)  # Alice's public key
    y = power_mod(G, b, P)  # Bob's public key
    print(f"\nAlice's Public Key (x = G^a mod P): {x}")
    print(f"Bob's Public Key (y = G^b mod P): {y}")

    # Step 4: Exchange public keys (x and y)

    # Step 5: Compute shared secret keys
    ka = power_mod(y, a, P)  # Alice computes secret key
    kb = power_mod(x, b, P)  # Bob computes secret key
    print(f"\nAlice's Computed Secret Key (y^a mod P): {ka}")
    print(f"Bob's Computed Secret Key (x^b mod P): {kb}")

    # Step 6: Confirm both secret keys are same
    if ka == kb:
        print(f"\nShared Secret Key is successfully established: {ka}")
    else:
        print("\nError: Secret keys do not match!")

if __name__ == "__main__":
    diffie_hellman_key_exchange()
