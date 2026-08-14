"""
Given a 2D matrix (list of lists), return a new matrix where each row
is reversed.
"""
def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix]


if __name__ == "__main__":
    test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mirrored = mirror_matrix(test_matrix)
    print(f"Original matrix: {test_matrix}")
    print(f"Mirrored matrix: {mirrored}")
