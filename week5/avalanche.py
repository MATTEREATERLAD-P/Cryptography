def feistel_encrypt_full(plaintext, keys):
    mid  = len(plaintext) // 2
    L, R = int(plaintext[:mid], 2), int(plaintext[mid:], 2)
    for key in keys:
        L, R = (R, L ^ ((R ^ key) % 256))
    return (L << 4) | R

def bit_difference(a, b, bits=8):
    return bin(a ^ b).count('1')

keys = [0b1010, 0b1100, 0b0110]
p1   = "10110100"
p2   = "10110101"  # 1-bit difference

c1 = feistel_encrypt_full(p1, keys)
c2 = feistel_encrypt_full(p2, keys)

diff = bit_difference(c1, c2)
print(f"Plaintext 1 : {p1}  → Ciphertext: {c1:08b}")
print(f"Plaintext 2 : {p2}  → Ciphertext: {c2:08b}")
print(f"Input diff  : 1 bit")
print(f"Output diff : {diff} bits")
print(f"Avalanche Effect: {'✅ Strong' if diff >= 3 else '⚠️ Weak'}")