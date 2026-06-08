def vigenere_cipher(text, key, encrypt=True):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            if not encrypt:
                shift = -shift
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

plaintext = "Hello World"
key = "SECRET"
ciphertext = vigenere_cipher(plaintext, key)
decrypted = vigenere_cipher(ciphertext, key, encrypt=False)
print(f"Plaintext:  {plaintext}")
print(f"Key:        {key}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted:  {decrypted}")