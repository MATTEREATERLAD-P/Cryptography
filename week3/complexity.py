def berlekamp_massey(s):
    n, L, m, b, C, B = len(s), 0, -1, 1, [1], [1]
    for n_idx in range(n):
        d = s[n_idx]
        for i in range(1, L + 1):
            if i < len(C):
                d ^= C[i] & s[n_idx - i]
        if d == 0:
            m += 1
        elif 2 * L <= n_idx:
            T  = C[:]
            p  = [0] * (n_idx - m)
            p += B
            C  = [c ^ p[i] if i < len(p) else c for i, c in enumerate(C + [0]*(len(p)-len(C)))]
            L  = n_idx + 1 - L
            B, m = T, n_idx
        else:
            p  = [0] * (n_idx - m)
            p += B
            C  = [c ^ p[i] if i < len(p) else c for i, c in enumerate(C + [0]*(len(p)-len(C)))]
            m += 1
    return L

import random
seq = [random.randint(0,1) for _ in range(50)]
lc  = berlekamp_massey(seq)
print(f"Sequence length  : {len(seq)}")
print(f"Linear Complexity: {lc}")
print(f"Expected (~n/2)  : {len(seq)//2}")