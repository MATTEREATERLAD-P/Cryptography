S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]
PERM  = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]

def spn_round(block, round_key):
    block = block ^ round_key
    print(f"After Key Mixing   : {block:016b}")
    nibbles = [(block >> (12 - 4*i)) & 0xF for i in range(4)]
    subst   = [S_BOX[n] for n in nibbles]
    block   = sum(subst[i] << (12 - 4*i) for i in range(4))
    print(f"After Substitution : {block:016b}")
    bits_in  = [(block >> (15-i)) & 1 for i in range(16)]
    bits_out = [0]*16
    for i, p in enumerate(PERM):
        bits_out[p] = bits_in[i]
    block = sum(bits_out[i] << (15-i) for i in range(16))
    print(f"After Permutation  : {block:016b}")
    return block

block = 0b0100111011011110
key   = 0b0011100010110111
print(f"Input Block: {block:016b}")
spn_round(block, key)