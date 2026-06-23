S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]

def encrypt(plaintext, key):
    return S_BOX[(plaintext ^ key) % 16]

def known_plaintext_attack(pairs):
    print("Known Plaintext Attack:")
    print(f"Using {len(pairs)} plaintext ciphertext pairs\n")
    for key in range(16):
        if all(encrypt(p, key) == c for p, c in pairs):
            print(f"Key Found: {key:04b} (decimal {key})")
            return
    print("Key not found")

true_key = 0b1001
pairs = [(i, encrypt(i, true_key)) for i in range(6)]
print("Plaintext   Ciphertext")
for p, c in pairs:
    print(f"{p:04b}        {c:04b}")
print()
known_plaintext_attack(pairs)