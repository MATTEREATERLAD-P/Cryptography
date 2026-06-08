from collections import Counter
import math

def chi_square_test(sequence, bins=8):
    n        = len(sequence)
    expected = n / bins
    counts   = Counter(x % bins for x in sequence)
    chi2     = sum((counts.get(i,0) - expected)**2 / expected for i in range(bins))
    print(f"Chi-Square Test:")
    print(f"  Chi² statistic : {chi2:.4f}")
    print(f"  Bins={bins}, Expected per bin={expected:.1f}")
    print("  Result: PASS ✅ (low chi²)" if chi2 < 15 else "  Result: FAIL ❌ (high chi²)")

import random
seq = [random.randint(0, 255) for _ in range(1000)]
chi_square_test(seq)