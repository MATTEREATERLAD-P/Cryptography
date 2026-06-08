S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]

def s_box_substitute(nibble):
    return S_BOX[nibble]

print("S-Box Substitution (Confusion):")
print(f"{'Input':>8} {'Output':>8} {'In (bin)':>10} {'Out (bin)':>10}")
for i in range(16):
    out = s_box_substitute(i)
    print(f"{i:>8} {out:>8}   {i:04b}      {out:04b}")