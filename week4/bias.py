import random
import matplotlib.pyplot as plt

def biased_prng(n, bias=0.6):
    return [1 if random.random() < bias else 0 for _ in range(n)]

def unbiased_prng(n):
    return [random.randint(0,1) for _ in range(n)]

n       = 1000
biased  = biased_prng(n)
uniform = unbiased_prng(n)

print(f"Biased PRNG  - Ones: {sum(biased)/n:.2%}  (expected ~60%)")
print(f"Uniform PRNG - Ones: {sum(uniform)/n:.2%} (expected ~50%)")

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(biased,  bins=2, color='red',   edgecolor='black', rwidth=0.5)
plt.title("Biased PRNG"); plt.xticks([0,1])

plt.subplot(1,2,2)
plt.hist(uniform, bins=2, color='green', edgecolor='black', rwidth=0.5)
plt.title("Uniform PRNG"); plt.xticks([0,1])

plt.tight_layout()
plt.savefig("fig5_bias_detection.png")
plt.show()