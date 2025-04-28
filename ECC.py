# ECC Algorithm Simple Implementation in Python

class ECC:
    def __init__(self, a, b, p):
        self.a = a  # coefficient of x
        self.b = b  # constant term
        self.p = p  # prime number for finite field

    def is_on_curve(self, point):
        if point is None:
            return True
        x, y = point
        return (y ** 2 - (x ** 3 + self.a * x + self.b)) % self.p == 0

    def point_add(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        
        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 != y2:
            return None

        if P == Q:
            # Slope (lambda) for point doubling
            m = (3 * x1 * x1 + self.a) * self.modinv(2 * y1, self.p)
        else:
            # Slope (lambda) for point addition
            m = (y2 - y1) * self.modinv(x2 - x1, self.p)
        
        m = m % self.p
        x3 = (m * m - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        
        return (x3, y3)

    def scalar_mult(self, k, P):
        result = None
        addend = P
        
        while k:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_add(addend, addend)
            k >>= 1
        return result

    def modinv(self, x, p):
        """Modular inverse using Extended Euclidean Algorithm"""
        return pow(x, -1, p)

# Example Usage
if __name__ == "__main__":
    # Define elliptic curve y^2 = x^3 + ax + b over finite field p
    a = 2
    b = 3
    p = 97  # prime number
    
    ecc = ECC(a, b, p)
    
    # Base point (generator)
    G = (3, 6)
    print(f"Base point G: {G}")

    # Private keys (selected randomly)
    private_key_A = 20
    private_key_B = 40
    print(f"\nPrivate Key of A: {private_key_A}")
    print(f"Private Key of B: {private_key_B}")

    # Public keys
    public_key_A = ecc.scalar_mult(private_key_A, G)
    public_key_B = ecc.scalar_mult(private_key_B, G)
    print(f"\nPublic Key of A: {public_key_A}")
    print(f"Public Key of B: {public_key_B}")

    # Shared secret generation
    shared_secret_A = ecc.scalar_mult(private_key_A, public_key_B)
    shared_secret_B = ecc.scalar_mult(private_key_B, public_key_A)
    print(f"\nShared Secret computed by A: {shared_secret_A}")
    print(f"Shared Secret computed by B: {shared_secret_B}")

    # Check if both shared secrets are the same
    if shared_secret_A == shared_secret_B:
        print(f"\nECC Key Exchange Successful. Shared Secret: {shared_secret_A}")
    else:
        print("\nKey Exchange Failed!")
