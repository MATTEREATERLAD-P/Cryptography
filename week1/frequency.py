import matplotlib.pyplot as plt
import string

def frequency_analysis(text):
    text = text.upper()
    freq = {char: 0 for char in string.ascii_uppercase}
    total = sum(1 for c in text if c.isalpha())
    for char in text:
        if char.isalpha():
            freq[char] += 1
    return {k: (v / total) * 100 for k, v in freq.items()}

ciphertext = "KHOOR ZRUOG WKLV LV D WHVW PHVVDJH HQFUBSWHG XVLQJ FDHVDU FLSKHU"
freq = frequency_analysis(ciphertext)

plt.figure(figsize=(14, 5))
plt.bar(freq.keys(), freq.values(), color='steelblue')
plt.title("Frequency Analysis of Ciphertext")
plt.xlabel("Letter")
plt.ylabel("Frequency (%)")
plt.tight_layout()
plt.savefig("fig3_frequency_analysis.png")
plt.show()
print("Frequency analysis chart saved.")