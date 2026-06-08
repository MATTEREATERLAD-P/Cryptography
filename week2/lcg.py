def lcg(seed, a=1664525, c=1013904223, m=2**32, n=10):
    values = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        values.append(x)
    return values

seed = 42
sequence = lcg(seed)
print("LCG Pseudorandom Sequence:")
for i, val in enumerate(sequence):
    print(f"  X{i+1} = {val}")