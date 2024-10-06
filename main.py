# Import the SparseMatrix class from your implementation file
# Assume that the SparseMatrix class and Node class are defined in `sparse_matrix.py`
from sparse_matrix import SparseMatrix

def test_sparse_matrix_operations():
    # Load matrices from files
    matrix1 = SparseMatrix(file_path='matrix1.txt')
    matrix2 = SparseMatrix(file_path='matrix2.txt')
    matrix3 = SparseMatrix(file_path='matrix3.txt')

    # Perform addition
    addition_result = matrix1.add(matrix2)
    print("Addition Result:")
    addition_result.display()

    # Perform subtraction
    subtraction_result = matrix1.subtract(matrix2)
    print("\nSubtraction Result:")
    subtraction_result.display()

    # Perform multiplication
    multiplication_result = matrix1.multiply(matrix3)
    print("\nMultiplication Result:")
    multiplication_result.display()

    # Expected outcomes for verification
    expected_addition = SparseMatrix(num_rows=4, num_cols=4)
    expected_addition.insert_element(0, 0, 4)
    expected_addition.insert_element(0, 1, 4)
    expected_addition.insert_element(1, 1, 2)
    expected_addition.insert_element(1, 2, 8)
    expected_addition.insert_element(2, 3, 6)
    expected_addition.insert_element(3, 3, 4)

    expected_subtraction = SparseMatrix(num_rows=4, num_cols=4)
    expected_subtraction.insert_element(0, 0, 2)
    expected_subtraction.insert_element(0, 1, 4)
    expected_subtraction.insert_element(1, 2, 2)
    expected_subtraction.insert_element(2, 3, 6)
    expected_subtraction.insert_element(1, 1, -2)
    expected_subtraction.insert_element(3, 3, -4)

    expected_multiplication = SparseMatrix(num_rows=4, num_cols=2)
    expected_multiplication.insert_element(0, 0, 3)
    expected_multiplication.insert_element(1, 0, 5)
    expected_multiplication.insert_element(1, 1, 10)

    # Validate addition result
    assert matrices_are_equal(addition_result, expected_addition), "Addition test failed"

    # Validate subtraction result
    assert matrices_are_equal(subtraction_result, expected_subtraction), "Subtraction test failed"

    # Validate multiplication result
    assert matrices_are_equal(multiplication_result, expected_multiplication), "Multiplication test failed"

    print("All tests passed!")


def matrices_are_equal(matrix1, matrix2):
    """
    Helper function to compare two sparse matrices.
    Returns True if they are equal, otherwise False.
    """
    if matrix1.num_rows != matrix2.num_rows or matrix1.num_cols != matrix2.num_cols:
        return False

    current1 = matrix1.head
    current2 = matrix2.head

    # Traverse both linked lists and compare each node
    while current1 and current2:
        if (current1.row != current2.row or
            current1.col != current2.col or
            current1.value != current2.value):
            return False
        current1 = current1.next
        current2 = current2.next

    # If one list is longer than the other, they are not equal
    if current1 or current2:
        return False

    return True


if __name__ == "__main__":
    # Run the test function
    test_sparse_matrix_operations()
