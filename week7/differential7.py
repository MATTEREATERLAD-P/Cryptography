S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]

def encrypt(plaintext, key):
    return S_BOX[(plaintext ^ key) % 16]

def differential_cryptanalysis(target_diff, output_diff):
    candidates = {}
    for key in range(16):
        count = 0
        for p1 in range(16):
            p2 = p1 ^ target_diff
            c1 = encrypt(p1, key)
            c2 = encrypt(p2, key)
            if c1 ^ c2 == output_diff:
                count += 1
        candidates[key] = count
    best_key = max(candidates, key=candidates.get)
    print("Differential Cryptanalysis Results:")
    for k, v in candidates.items():
        print(f"Key {k:04b}: Score {v}")
    print(f"\nMost Likely Key: {best_key:04b}")

differential_cryptanalysis(0b0010, 0b1010)