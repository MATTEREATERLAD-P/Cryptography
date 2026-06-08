import math
from collections import Counter

def shannon_entropy(text):
    text = [c for c in text if c.isalpha()]
    total = len(text)
    counts = Counter(text)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return entropy

plaintext  = "Hello World This Is A Test Message"
ciphertext = "Khoor Zruog Wklv Lv D Whvw Phvvdjh"

e_plain  = shannon_entropy(plaintext)
e_cipher = shannon_entropy(ciphertext)

print(f"Plaintext Entropy:   {e_plain:.4f} bits")
print(f"Ciphertext Entropy:  {e_cipher:.4f} bits")
print(f"Difference:          {abs(e_cipher - e_plain):.4f} bits")