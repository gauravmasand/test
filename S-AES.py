# Simplified AES (S-AES) Implementation

# S-box and Inverse S-box
SBOX = [
    [0x9, 0x4, 0xA, 0xB],
    [0xD, 0x1, 0x8, 0x5],
    [0x6, 0x2, 0x0, 0x3],
    [0xC, 0xE, 0xF, 0x7]
]

SBOX_INV = [
    [0xA, 0x5, 0x9, 0xB],
    [0x1, 0x7, 0x8, 0xF],
    [0x6, 0x0, 0x2, 0x3],
    [0xC, 0x4, 0xD, 0xE]
]

# Helper functions
def nibble_substitution(nibble, sbox):
    row = (nibble & 0b1100) >> 2
    col = nibble & 0b0011
    return sbox[row][col]

def shift_rows(state):
    return [state[0], state[1], state[3], state[2]]

def shift_rows_inv(state):
    return [state[0], state[1], state[3], state[2]]

def mix_columns(state):
    return [
        state[0] ^ gf_mult(4, state[2]),
        state[1] ^ gf_mult(4, state[3]),
        state[2] ^ gf_mult(4, state[0]),
        state[3] ^ gf_mult(4, state[1])
    ]

def mix_columns_inv(state):
    return [
        state[0] ^ gf_mult(9, state[2]),
        state[1] ^ gf_mult(9, state[3]),
        state[2] ^ gf_mult(9, state[0]),
        state[3] ^ gf_mult(9, state[1])
    ]

def gf_mult(a, b):
    # Multiply two numbers in GF(2^4)
    p = 0
    for i in range(4):
        if b & 0x1:
            p ^= a
        high_bit_set = a & 0x8
        a <<= 1
        if high_bit_set:
            a ^= 0b11  # x^4 + x + 1
        b >>= 1
    return p & 0xF

# Key expansion
def key_expansion(key):
    rcon1 = 0b1000
    rcon2 = 0b0011

    w = [0] * 6
    w[0] = (key & 0xFF00) >> 8
    w[1] = key & 0x00FF

    w[2] = w[0] ^ rcon1 ^ (nibble_substitution(w[1] >> 4, SBOX) << 4 | nibble_substitution(w[1] & 0xF, SBOX))
    w[3] = w[2] ^ w[1]
    
    w[4] = w[2] ^ rcon2 ^ (nibble_substitution(w[3] >> 4, SBOX) << 4 | nibble_substitution(w[3] & 0xF, SBOX))
    w[5] = w[4] ^ w[3]

    return [w[0], w[1], w[2], w[3], w[4], w[5]]

def add_round_key(state, key):
    return [s ^ k for s, k in zip(state, key)]

# Encrypt one block (16 bits)
def encrypt_block(plain, key):
    w = key_expansion(key)

    state = [
        (plain & 0xF000) >> 12,
        (plain & 0x0F00) >> 8,
        (plain & 0x00F0) >> 4,
        (plain & 0x000F)
    ]
    
    state = add_round_key(state, [w[0] >> 4, w[0] & 0xF, w[1] >> 4, w[1] & 0xF])

    # Round 1
    state = [nibble_substitution(n, SBOX) for n in state]
    state = shift_rows(state)
    state = mix_columns(state)
    state = add_round_key(state, [w[2] >> 4, w[2] & 0xF, w[3] >> 4, w[3] & 0xF])

    # Round 2
    state = [nibble_substitution(n, SBOX) for n in state]
    state = shift_rows(state)
    state = add_round_key(state, [w[4] >> 4, w[4] & 0xF, w[5] >> 4, w[5] & 0xF])

    cipher = (state[0] << 12) | (state[1] << 8) | (state[2] << 4) | state[3]
    return cipher

def decrypt_block(cipher, key):
    w = key_expansion(key)

    state = [
        (cipher & 0xF000) >> 12,
        (cipher & 0x0F00) >> 8,
        (cipher & 0x00F0) >> 4,
        (cipher & 0x000F)
    ]

    # Reverse Round 2
    state = add_round_key(state, [w[4] >> 4, w[4] & 0xF, w[5] >> 4, w[5] & 0xF])
    state = shift_rows_inv(state)
    state = [nibble_substitution(n, SBOX_INV) for n in state]

    # Reverse Round 1
    state = add_round_key(state, [w[2] >> 4, w[2] & 0xF, w[3] >> 4, w[3] & 0xF])
    state = mix_columns_inv(state)
    state = shift_rows_inv(state)
    state = [nibble_substitution(n, SBOX_INV) for n in state]

    # Initial key addition
    state = add_round_key(state, [w[0] >> 4, w[0] & 0xF, w[1] >> 4, w[1] & 0xF])

    plain = (state[0] << 12) | (state[1] << 8) | (state[2] << 4) | state[3]
    return plain

# Example Usage
if __name__ == "__main__":
    plaintext = 0b1101011100101000  # 16 bits
    key = 0b0100101011110101        # 16 bits

    print(f"Plaintext: {bin(plaintext)}")
    print(f"Key: {bin(key)}")

    ciphertext = encrypt_block(plaintext, key)
    print(f"Ciphertext: {bin(ciphertext)}")

    decrypted = decrypt_block(ciphertext, key)
    print(f"Decrypted: {bin(decrypted)}")
