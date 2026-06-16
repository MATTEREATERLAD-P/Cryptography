S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]
PERM  = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]

def spn_round(block, key):
    block ^= key
    nibbles = [(block >> (12-4*i)) & 0xF for i in range(4)]
    subst   = [S_BOX[n] for n in nibbles]
    block   = sum(subst[i] << (12-4*i) for i in range(4))
    bits_in  = [(block >> (15-i)) & 1 for i in range(16)]
    bits_out = [0]*16
    for i, p in enumerate(PERM):
        bits_out[p] = bits_in[i]
    return sum(bits_out[i] << (15-i) for i in range(16))

key = 0b0011100010110111
p1  = 0b0100111011011110
p2  = 0b0100111011011111

c1   = spn_round(p1, key)
c2   = spn_round(p2, key)
diff = bin(c1 ^ c2).count('1')

print(f"Plaintext 1 : {p1:016b}")
print(f"Plaintext 2 : {p2:016b}")
print(f"Ciphertext 1: {c1:016b}")
print(f"Ciphertext 2: {c2:016b}")
print(f"Bits Changed: {diff} out of 16")
print("Strong Avalanche Effect" if diff >= 4 else "Weak Avalanche Effect")