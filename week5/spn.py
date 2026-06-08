S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]
PERM  = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]

def spn_round(block, round_key):
    # Key mixing
    block = block ^ round_key
    # Substitution (4-bit nibbles)
    nibbles   = [(block >> (12 - 4*i)) & 0xF for i in range(4)]
    subst     = [S_BOX[n] for n in nibbles]
    block     = sum(subst[i] << (12 - 4*i) for i in range(4))
    # Permutation
    bits_in   = [(block >> (15-i)) & 1 for i in range(16)]
    bits_out  = [0]*16
    for i, p in enumerate(PERM):
        bits_out[p] = bits_in[i]
    block = sum(bits_out[i] << (15-i) for i in range(16))
    return block

plaintext  = 0b0100111011011110
round_keys = [0b0011100010110111, 0b1001011101000010]

block = plaintext
print(f"Plaintext : {block:016b}")
for r, rk in enumerate(round_keys):
    block = spn_round(block, rk)
    print(f"Round {r+1}  : {block:016b}")
print(f"Ciphertext: {block:016b}")