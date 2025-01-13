def input_matrix(rows, cols, name):
    print(f"Enter the elements of matrix {name} row by row (n n n):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Please enter exactly {cols} numbers for this row (n n n).")
            return input_matrix(rows, cols, name)
        matrix.append(row)
    return matrix

# Dimensions of the matrices
rows = 3
cols = 3

# Input matrices
X = input_matrix(rows, cols, "X")
Y = input_matrix(rows, cols, "Y")

# Initialize the result matrix
result = [[0 for _ in range(cols)] for _ in range(rows)]

# Add the matrices
for i in range(rows):
    for j in range(cols):
        result[i][j] = X[i][j] - Y[i][j]

# Print the result
print("\nResultant Matrix:")
for r in result:
    print(r)