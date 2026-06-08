def lfsr_stream(seed, taps, length):
    state  = seed[:]
    output = []
    for _ in range(length):
        output.append(state[-1])
        fb = 0
        for t in taps:
            fb ^= state[t]
        state = [fb] + state[:-1]
    return output

def correlation_attack(observed, candidates):
    best_corr, best_seed = 0, None
    for seed in candidates:
        stream = lfsr_stream(list(seed), [0,3], len(observed))
        corr   = sum(a == b for a, b in zip(observed, stream)) / len(observed)
        if corr > best_corr:
            best_corr, best_seed = corr, seed
    return best_seed, best_corr

import itertools
true_seed  = [1,0,1,1]
observed   = lfsr_stream(true_seed, [0,3], 20)
candidates = list(itertools.product([0,1], repeat=4))
found, corr = correlation_attack(observed, candidates)

print(f"True seed  : {true_seed}")
print(f"Found seed : {list(found)}")
print(f"Correlation: {corr:.2%}")