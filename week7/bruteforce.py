import time

S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]

def encrypt(plaintext, key):
    return S_BOX[(plaintext ^ key) % 16]

def brute_force(pairs, key_space):
    start = time.time()
    for key in range(key_space):
        if all(encrypt(p, key % 16) == c for p, c in pairs):
            elapsed = time.time() - start
            print(f"Key Found     : {key:04b}")
            print(f"Keys Tested   : {key + 1}")
            print(f"Key Space     : {key_space}")
            print(f"Time Taken    : {elapsed:.6f} seconds")
            return
    print("Key not found in given key space")

true_key = 0b0111
pairs    = [(i, encrypt(i, true_key)) for i in range(4)]
print("Brute Force Attack on Block Cipher\n")
brute_force(pairs, 256)