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



if __name__ == "__main__":
    # testing
    test_sparse_matrix_operations()
