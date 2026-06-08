import os

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

plaintext = b"HelloWorld"
key       = os.urandom(len(plaintext))  # True random key
ciphertext = xor_bytes(plaintext, key)
decrypted  = xor_bytes(ciphertext, key)

print(f"Plaintext:  {plaintext}")
print(f"Key:        {key.hex()}")
print(f"Ciphertext: {ciphertext.hex()}")
print(f"Decrypted:  {decrypted}")