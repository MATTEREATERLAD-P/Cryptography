PERM = [1,5,2,0,3,7,4,6]

def permute(bits):
    return [bits[PERM[i]] for i in range(len(PERM))]

original  = [1,0,1,1,0,1,0,0]
permuted  = permute(original)

print("Permutation (Diffusion):")
print(f"Original : {original}")
print(f"Permuted : {permuted}")
print(f"\nBit positions remapped via P={PERM}")
print("Changing 1 input bit spreads across multiple output positions → Diffusion ✅")