S_BOX = [0x6,0x4,0xC,0x5,0x0,0x7,0x2,0xE,
         0x1,0xF,0x3,0xD,0x8,0xA,0x9,0xB]

def differential_uniformity(s_box):
    n = len(s_box)
    top_count = 0
    for dx in range(1, n):
        counts = {}
        for x in range(n):
            dy = s_box[x] ^ s_box[x ^ dx]
            counts[dy] = counts.get(dy, 0) + 1
        for dy, count in counts.items():
            if count > top_count:
                top_count = count
            print(f"Input Diff: {dx:04b}  Output Diff: {dy:04b}  Count: {count}")
    print(f"\nHighest Differential Count: {top_count}")
    print("Lower value means better resistance to differential attacks")

differential_uniformity(S_BOX)