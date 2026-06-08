def autocorrelation_test(sequence, lag=1):
    n      = len(sequence)
    mean   = sum(sequence) / n
    c0     = sum((x - mean)**2 for x in sequence) / n
    ck     = sum((sequence[i] - mean) * (sequence[i+lag] - mean)
                  for i in range(n - lag)) / n
    result = ck / c0
    print(f"Autocorrelation (lag={lag}): {result:.4f}")
    print("  Close to 0 → Low correlation → Good randomness ✅" if abs(result) < 0.1
          else "  High correlation detected ❌")

import random
seq = [random.randint(0, 1) for _ in range(500)]
autocorrelation_test(seq, lag=1)
autocorrelation_test(seq, lag=5)