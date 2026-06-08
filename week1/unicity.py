def unicity_distance(key_space_bits, redundancy_per_char):
    """
    key_space_bits      : e.g. log2(26) for Caesar = ~4.7 bits
    redundancy_per_char : English redundancy ~3.2 bits/char
    """
    unicity = key_space_bits / redundancy_per_char
    return unicity

import math

print("=== Unicity Distance Calculator ===\n")

# Caesar Cipher
caesar_keys   = math.log2(26)
redundancy    = 3.2
ud_caesar     = unicity_distance(caesar_keys, redundancy)
print(f"Caesar Cipher:")
print(f"  Key space     : log2(26) = {caesar_keys:.2f} bits")
print(f"  Redundancy    : {redundancy} bits/char")
print(f"  Unicity Dist. : {ud_caesar:.2f} characters\n")

# Vigenère (key length 6)
vigenere_keys = math.log2(26**6)
ud_vigenere   = unicity_distance(vigenere_keys, redundancy)
print(f"Vigenère Cipher (key length 6):")
print(f"  Key space     : log2(26^6) = {vigenere_keys:.2f} bits")
print(f"  Redundancy    : {redundancy} bits/char")
print(f"  Unicity Dist. : {ud_vigenere:.2f} characters")