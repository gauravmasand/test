# S-DES Implementation in Python

# Permutation functions
def permute(bits, pattern):
    return [bits[p - 1] for p in pattern]

# Left shift function
def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

# S-boxes
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2],
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3],
]

# Key generation
def generate_keys(key):
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]

    key = permute(key, p10)
    left, right = key[:5], key[5:]
    
    left = left_shift(left, 1)
    right = left_shift(right, 1)
    k1 = permute(left + right, p8)
    
    left = left_shift(left, 2)
    right = left_shift(right, 2)
    k2 = permute(left + right, p8)
    
    return k1, k2

# Initial and inverse initial permutation
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]

# Expansion permutation
EP = [4, 1, 2, 3, 2, 3, 4, 1]

# Permutation P4
P4 = [2, 4, 3, 1]

def sbox_lookup(bits, sbox):
    row = (bits[0] << 1) + bits[3]
    col = (bits[1] << 1) + bits[2]
    val = sbox[row][col]
    return [(val & 0b10) >> 1, val & 0b1]

def fk(bits, key):
    left, right = bits[:4], bits[4:]
    expanded = permute(right, EP)
    temp = [e ^ k for e, k in zip(expanded, key)]
    
    left_sbox = sbox_lookup(temp[:4], S0)
    right_sbox = sbox_lookup(temp[4:], S1)
    
    combined = left_sbox + right_sbox
    combined = permute(combined, P4)
    
    result = [l ^ c for l, c in zip(left, combined)]
    return result + right

def switch(bits):
    return bits[4:] + bits[:4]

def encrypt(plaintext, key):
    k1, k2 = generate_keys(key)
    bits = permute(plaintext, IP)
    bits = fk(bits, k1)
    bits = switch(bits)
    bits = fk(bits, k2)
    ciphertext = permute(bits, IP_inv)
    return ciphertext

def decrypt(ciphertext, key):
    k1, k2 = generate_keys(key)
    bits = permute(ciphertext, IP)
    bits = fk(bits, k2)
    bits = switch(bits)
    bits = fk(bits, k1)
    plaintext = permute(bits, IP_inv)
    return plaintext

# Helper functions
def str_to_bits(s):
    return [int(c) for c in s]

def bits_to_str(b):
    return ''.join(str(bit) for bit in b)

# Example Usage
if __name__ == "__main__":
    plaintext = "10111101"  # 8 bits
    key = "1010000010"      # 10 bits
    
    plaintext_bits = str_to_bits(plaintext)
    key_bits = str_to_bits(key)
    
    encrypted = encrypt(plaintext_bits, key_bits)
    decrypted = decrypt(encrypted, key_bits)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Key:        {key}")
    print(f"Encrypted:  {bits_to_str(encrypted)}")
    print(f"Decrypted:  {bits_to_str(decrypted)}")
