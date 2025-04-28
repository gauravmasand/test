# RSA Algorithm Implementation in Python

def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    """Compute the modular multiplicative inverse of e modulo phi"""
    d_old, d = 0, 1
    r_old, r = phi, e
    while r != 0:
        quotient = r_old // r
        d_old, d = d, d_old - quotient * d
        r_old, r = r, r_old - quotient * r
    return d_old % phi

def rsa_key_generation(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) are not coprime. Choose a different e.")
    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(message, pub_key):
    e, n = pub_key
    ciphertext = pow(message, e, n)
    return ciphertext

def decrypt(ciphertext, priv_key):
    d, n = priv_key
    message = pow(ciphertext, d, n)
    return message

# Example Usage
if __name__ == "__main__":
    # Step 1: Select primes
    p = 53
    q = 59
    e = 3

    print(f"Selected primes: p = {p}, q = {q}")
    print(f"Selected public exponent: e = {e}")

    # Step 2: Key generation
    public_key, private_key = rsa_key_generation(p, q, e)
    print(f"\nPublic Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")

    # Step 3: Encrypting the message "HI"
    # Convert 'H' = 8, 'I' = 9 into a two-digit number: 89
    message = 89
    print(f"\nOriginal Message (numeric): {message}")

    ciphertext = encrypt(message, public_key)
    print(f"Encrypted Message: {ciphertext}")

    decrypted_message = decrypt(ciphertext, private_key)
    print(f"Decrypted Message: {decrypted_message}")

    # Final output
    print("\nDecrypted characters:")
    print(f"First character: {decrypted_message // 10} -> 'H'")
    print(f"Second character: {decrypted_message % 10} -> 'I'")
