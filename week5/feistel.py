def feistel_round(left, right, round_key):
    def F(r, k):
        return (r ^ k) % 256
    new_left  = right
    new_right = left ^ F(right, round_key)
    return new_left, new_right

def feistel_encrypt(plaintext, keys):
    mid   = len(plaintext) // 2
    L, R  = int(plaintext[:mid], 2), int(plaintext[mid:], 2)
    print(f"Initial: L={L:04b}, R={R:04b}")
    for i, key in enumerate(keys):
        L, R = feistel_round(L, R, key)
        print(f"Round {i+1}: L={L:04b}, R={R:04b}")
    return L, R

def feistel_decrypt(L, R, keys):
    print(f"\nDecryption:")
    for key in reversed(keys):
        R, L = feistel_round(R, L, key)
    return L, R

plaintext = "10110100"
keys      = [0b1010, 0b1100, 0b0110]
L, R      = feistel_encrypt(plaintext, keys)
print(f"Ciphertext: L={L:04b}, R={R:04b}")
dL, dR    = feistel_decrypt(L, R, keys)
print(f"Decrypted:  L={dL:04b}, R={dR:04b}")