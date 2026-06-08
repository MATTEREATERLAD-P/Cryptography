import random
import os
import matplotlib.pyplot as plt

pseudo = [random.randint(0, 255) for _ in range(256)]
true_r = list(os.urandom(256))

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(pseudo, color='blue', linewidth=0.8)
plt.title("Pseudorandom (Python random)")
plt.xlabel("Index"); plt.ylabel("Value")

plt.subplot(1, 2, 2)
plt.plot(true_r, color='green', linewidth=0.8)
plt.title("True Random (os.urandom)")
plt.xlabel("Index"); plt.ylabel("Value")

plt.tight_layout()
plt.savefig("fig5_randomness_comparison.png")
plt.show()