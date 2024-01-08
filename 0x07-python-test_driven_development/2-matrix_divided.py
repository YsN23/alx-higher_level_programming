#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Dividing Elements of a matrix by div"""

    new_mat = []

    first_row_size = len(matrix[0])

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row1 in matrix:
        if not isinstance(row1, list):
            raise TypeError("Each row in the matrix must be a list")

        if len(row1) != first_row_size:
            raise TypeError("Each row of the matrix must have the same size")


        new_row = []
        for elem in row1:

            if not isinstance(row1, list) and not (isinstance(elem, int) or isinstance(elem, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            result_div = elem / div
            formatted_result = "{:.2f}".format(result_div)
            formatted_result = float(formatted_result)
            new_row.append(formatted_result)
        new_mat.append(new_row)

    return new_mat
