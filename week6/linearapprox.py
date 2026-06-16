S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]

def linear_approximation_table(s_box):
    n = len(s_box)
    print(f"{'':>4}", end="")
    for b in range(n):
        print(f"{b:>4}", end="")
    print()
    for a in range(n):
        print(f"{a:>4}", end="")
        for b in range(n):
            bias = sum((-1)**(bin(a & x).count('1') ^ bin(b & s_box[x]).count('1'))
                      for x in range(n))
            print(f"{bias:>4}", end="")
        print()

linear_approximation_table(S_BOX)