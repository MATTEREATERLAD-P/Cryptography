def simple_algebraic_attack(equations, variables=4):
    """Demonstrates solving a simple system of binary linear equations."""
    print("Solving system of binary equations (GF(2)):")
    for i, eq in enumerate(equations):
        print(f"  Eq {i+1}: {eq}")
    # Simple Gaussian elimination in GF(2)
    matrix = [list(row) for row in equations]
    n      = len(matrix[0]) - 1
    for col in range(n):
        pivot = next((r for r in range(col, len(matrix)) if matrix[r][col] == 1), None)
        if pivot is None:
            continue
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        for row in range(len(matrix)):
            if row != col and matrix[row][col] == 1:
                matrix[row] = [matrix[row][i] ^ matrix[col][i] for i in range(len(matrix[row]))]
    solution = [matrix[i][-1] for i in range(n)]
    print(f"\nSolution (key bits): {solution}")

equations = [
    [1,1,0,0,1],
    [0,1,1,0,0],
    [1,0,1,1,1],
    [0,0,1,1,0],
]
simple_algebraic_attack(equations)