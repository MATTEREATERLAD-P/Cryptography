S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]

def encrypt(plaintext, key):
    return S_BOX[(plaintext ^ key) % 16]

def linear_cryptanalysis(pairs, a, b):
    key_bias = {}
    for key in range(16):
        bias = 0
        for p, c in pairs:
            lhs = bin(p & a).count('1') % 2
            rhs = bin(c & b).count('1') % 2
            if lhs == rhs:
                bias += 1
        key_bias[key] = abs(bias - len(pairs) // 2)
    best_key = max(key_bias, key=key_bias.get)
    print("Linear Cryptanalysis Results:")
    for k, v in key_bias.items():
        print(f"Key {k:04b}: Bias {v}")
    print(f"\nMost Likely Key: {best_key:04b}")

import random
true_key = 0b0101
pairs = [(p, encrypt(p, true_key)) for p in random.sample(range(16), 8)]
linear_cryptanalysis(pairs, 0b0011, 0b0101)