def lfsr(seed, taps, length=20):
    state = seed[:]
    output = []
    for _ in range(length):
        output.append(state[-1])
        feedback = 0
        for t in taps:
            feedback ^= state[t]
        state = [feedback] + state[:-1]
    return output

seed   = [1, 0, 1, 1]
taps   = [0, 3]
seq    = lfsr(seed, taps)
print(f"LFSR Output Sequence: {seq}")
print(f"Period observed: {len(seq)}")
