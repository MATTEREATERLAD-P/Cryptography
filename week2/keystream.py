def keystream_encrypt(plaintext, key):
    key_repeated = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    ciphertext   = [ord(p) ^ ord(k) for p, k in zip(plaintext, key_repeated)]
    return ciphertext

def keystream_decrypt(ciphertext, key):
    key_repeated = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    plaintext    = ''.join(chr(c ^ ord(k)) for c, k in zip(ciphertext, key_repeated))
    return plaintext

plaintext  = "SecureMessage"
key        = "KEY"
ciphertext = keystream_encrypt(plaintext, key)
decrypted  = keystream_decrypt(ciphertext, key)

print(f"Plaintext:  {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted:  {decrypted}")