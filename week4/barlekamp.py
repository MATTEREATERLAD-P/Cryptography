def berlekamp_massey_verbose(s):
    print(f"Input sequence: {s}\n")
    n, L, m, b, C, B = len(s), 0, -1, 1, [1], [1]
    for n_idx in range(n):
        d = s[n_idx]
        for i in range(1, L+1):
            if i < len(C):
                d ^= C[i] & s[n_idx-i]
        print(f"Step {n_idx+1}: discrepancy d={d}, L={L}, LFSR={C}")
        if d != 0 and 2*L <= n_idx:
            T = C[:]
            p = [0]*(n_idx-m) + B
            C = [c ^ (p[i] if i < len(p) else 0) for i, c in enumerate(C + [0]*max(0, len(p)-len(C)))]
            L, B, m = n_idx+1-L, T, n_idx
    print(f"\nFinal LFSR length (Linear Complexity): {L}")
    return L

s = [1,0,1,1,0,1,0,0]
berlekamp_massey_verbose(s)