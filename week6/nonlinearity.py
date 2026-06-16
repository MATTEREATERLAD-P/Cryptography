S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]

def nonlinearity(s_box):
    n = len(s_box)
    max_bias = 0
    for a in range(n):
        for b in range(1, n):
            bias = abs(sum((-1)**(bin(a & x).count('1') ^ bin(b & s_box[x]).count('1'))
                       for x in range(n)))
            if bias > max_bias:
                max_bias = bias
    return (n - max_bias) // 2

print(f"S Box: {S_BOX}")
print(f"Nonlinearity Score: {nonlinearity(S_BOX)}")
print("Higher score means stronger resistance to linear cryptanalysis")