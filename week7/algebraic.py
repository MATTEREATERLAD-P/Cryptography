def gaussian_elimination_gf2(matrix):
    n = len(matrix)
    for col in range(n):
        pivot = next((r for r in range(col, n) if matrix[r][col] == 1), None)
        if pivot is None:
            continue
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        for row in range(n):
            if row != col and matrix[row][col] == 1:
                matrix[row] = [matrix[row][i] ^ matrix[col][i]
                               for i in range(len(matrix[row]))]
    solution = [matrix[i][-1] for i in range(n)]
    return solution

equations = [
    [1,0,1,1,1],
    [0,1,1,0,0],
    [1,1,0,1,0],
    [0,1,0,1,1],
]

print("Algebraic Attack over GF(2):")
print("Solving system of binary equations...\n")
solution = gaussian_elimination_gf2(equations)
print(f"Recovered Key Bits: {solution}")