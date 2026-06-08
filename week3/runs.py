def runs_test(sequence):
    n    = len(sequence)
    ones = sum(sequence)
    pi   = ones / n
    runs = 1 + sum(1 for i in range(1, n) if sequence[i] != sequence[i-1])
    expected = 2 * n * pi * (1 - pi)
    variance = 4 * n * pi**2 * (1 - pi)**2  # simplified
    import math
    z = (runs - expected) / (variance ** 0.5)
    print(f"Runs Test:")
    print(f"  Total runs   : {runs}")
    print(f"  Expected runs: {expected:.2f}")
    print(f"  Z-score      : {z:.4f}")

import random
bits = [random.randint(0,1) for _ in range(1000)]
runs_test(bits)
