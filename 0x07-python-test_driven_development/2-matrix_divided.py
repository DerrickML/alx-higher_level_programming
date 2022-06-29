#!/usr/bin/python3

"""This is the "2-matrix_divided.py" module.
This module supplies one function, matrix_divided(matrix, div)"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix by div
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("div must be a number")

    if matrix is None:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix[0]) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    else:
        rows = len(matrix)
        colums = len(matrix[0])

        new_matrix = [[0 for i in range(colums)] for j in range(rows)]
        # print(new_matrix)

        for r in range(rows):
            for c in range(colums):
                n = matrix[r][c]

                if not isinstance(n, int) and not isinstance(n, float):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of \
                            integers/floats")
                else:
                    new_matrix[r][c] = float("%0.2f" % (n / div))

        return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print(matrix_divided(matrix, 3))
    print(matrix)
