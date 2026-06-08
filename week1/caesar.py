def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

plaintext = "Hello World"
shift = 3
ciphertext = caesar_cipher(plaintext, shift)
print(f"Plaintext:  {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted:  {caesar_cipher(ciphertext, -shift)}")