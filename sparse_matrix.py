class Node:
    """
    A class to represent a node in the linked list.
    Each node stores a non-zero matrix entry.
    """

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.next = None


class SparseMatrix:
    """
    A class to represent a sparse matrix using a linked list.
    Supports addition, subtraction, and multiplication operations.
    """

    def __init__(self, num_rows=None, num_cols=None, file_path=None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.head = None

        # If file_path is provided, read the matrix from the file
        if file_path:
            self.read_from_file(file_path)

    def read_from_file(self, file_path):
        """
        Reads a sparse matrix from a file and populates the linked list.
        The file is expected to have the following format:
        rows=8433
        cols=3180
        (0, 381, -694)
        (0, 128, -838)
        """
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()

                # Parse the first two lines for rows and columns
                self.num_rows = int(lines[0].strip().split('=')[1])
                self.num_cols = int(lines[1].strip().split('=')[1])

                # Parse the remaining lines for matrix elements
                for line in lines[2:]:
                    # Skip empty lines
                    if not line.strip():
                        continue

                    # Parse each element line (e.g., "(0, 381, -694)")
                    row, col, value = self._parse_element(line.strip())
                    self.insert_element(row, col, value)

        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except ValueError:
            raise ValueError(f"Error in parsing file: {file_path}")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")

    def _parse_element(self, line):
        """
        Parses a single line representing a matrix element, e.g., "(0, 381, -694)"
        Returns the row, column, and value as integers.
        """
        try:
            # Remove parentheses and split by commas
            line = line.replace("(", "").replace(")", "")
            row, col, value = map(int, line.split(','))
            return row, col, value
        except Exception:
            raise ValueError(f"Input file has wrong format")

    def insert_element(self, row, col, value):
        """
        Inserts an element (row, col, value) into the linked list.
        """
        if value == 0:
            return  # We don't store zero values

        new_node = Node(row, col, value)

        # If the list is empty, set head to the new node
        if not self.head:
            self.head = new_node
            return

        # Traverse to the end of the linked list and insert the new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def get_element(self, row, col):
        """
        Retrieves the value at the specified row and column.
        Returns 0 if the element is not in the linked list.
        """
        current = self.head
        while current:
            if current.row == row and current.col == col:
                return current.value
            current = current.next
        return 0  # Default to zero if not found

    def set_element(self, row, col, value):
        """
        Sets the value at the specified row and column.
        Updates the value if the element is already present, or inserts it otherwise.
        """
        # If the value is zero, we don't store it in the linked list
        if value == 0:
            return

        # Check if the element already exists and update it
        current = self.head
        while current:
            if current.row == row and current.col == col:
                current.value = value
                return
            current = current.next

        # If element does not exist, insert a new one
        self.insert_element(row, col, value)

    def add(self, other):
        """
        Adds this matrix with another matrix and returns the resulting matrix.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for addition")

        result = SparseMatrix(self.num_rows, self.num_cols)

        # Traverse both matrices and add elements
        current = self.head
        while current:
            result.set_element(current.row, current.col, current.value)
            current = current.next

        current = other.head
        while current:
            existing_value = result.get_element(current.row, current.col)
            result.set_element(current.row, current.col, existing_value + current.value)
            current = current.next

        return result

    def subtract(self, other):
        """
        Subtracts another matrix from this matrix and returns the resulting matrix.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for subtraction")

        result = SparseMatrix(self.num_rows, self.num_cols)

        # Traverse both matrices and subtract elements
        current = self.head
        while current:
            result.set_element(current.row, current.col, current.value)
            current = current.next

        current = other.head
        while current:
            existing_value = result.get_element(current.row, current.col)
            result.set_element(current.row, current.col, existing_value - current.value)
            current = current.next

        return result

    def multiply(self, other):
        """
        Multiplies this matrix with another matrix and returns the resulting matrix.
        """
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices dimensions do not match for multiplication")

        result = SparseMatrix(self.num_rows, other.num_cols)

        # Implement matrix multiplication
        current = self.head
        while current:
            other_current = other.head
            while other_current:
                if current.col == other_current.row:
                    # Multiply elements and add to the result matrix
                    existing_value = result.get_element(current.row, other_current.col)
                    result.set_element(current.row, other_current.col,
                                       existing_value + (current.value * other_current.value))
                other_current = other_current.next
            current = current.next

        return result

    def display(self):
        """
        Displays the sparse matrix elements.
        """
        current = self.head
        while current:
            print(f"({current.row}, {current.col}) = {current.value}")
            current = current.next