def stream_cipher_encrypt(plaintext_bytes, keystream):
    return bytes(p ^ k for p, k in zip(plaintext_bytes, keystream))

# Simulating known plaintext attack
plaintext  = b"ATTACK"
keystream  = bytes([0x3A, 0x7F, 0x2B, 0x91, 0x04, 0xC8])
ciphertext = stream_cipher_encrypt(plaintext, keystream)

# Attacker knows plaintext + ciphertext → recovers keystream
recovered_keystream = bytes(c ^ p for c, p in zip(ciphertext, plaintext))

print(f"Plaintext          : {plaintext}")
print(f"Keystream          : {keystream.hex()}")
print(f"Ciphertext         : {ciphertext.hex()}")
print(f"Recovered Keystream: {recovered_keystream.hex()}")
print(f"Match: {'✅ YES' if recovered_keystream == keystream else '❌ NO'}")
