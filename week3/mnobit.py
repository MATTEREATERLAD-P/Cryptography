def monobit_test(sequence):
    n = len(sequence)
    s = sum(1 if b == 1 else -1 for b in sequence)
    s_obs = abs(s) / (n ** 0.5)
    import math
    p_value = math.erfc(s_obs / (2 ** 0.5))
    passed  = p_value >= 0.01
    print(f"Monobit Test:")
    print(f"  n={n}, S={s}, S_obs={s_obs:.4f}")
    print(f"  P-value={p_value:.4f} → {'PASS ✅' if passed else 'FAIL ❌'}")

import random
bits = [random.randint(0,1) for _ in range(1000)]
monobit_test(bits)