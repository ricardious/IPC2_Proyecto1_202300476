class MatrixNode:
    """
    A class to represent a node in a matrix row.
    Each node holds a value and a reference to the next node in the row.
    """
    def __init__(self, value=0):
        """
        Initializes a MatrixNode with the given value.

        Args:
            value (int, optional): The value to be stored in the node. Defaults to 0.
        """
        self.value = value
        self.next = None


class MatrixRow:
    """
    A class to represent a row in a matrix.
    Each row is a linked list of MatrixNode objects.
    """
    def __init__(self):
        """
        Initializes an empty MatrixRow.
        """
        self.head = None
        self.tail = None
        self.next = None


class Matrix:
    """
    A class to represent a matrix.
    The matrix is composed of rows, each of which is a linked list of nodes.
    """
    def __init__(self, name, n, m):
        """
        Initializes a Matrix with a given name, number of rows, and columns.

        Args:
            name (str): The name of the matrix.
            n (int): The number of rows in the matrix.
            m (int): The number of columns in the matrix.
        """
        self.name = name
        self.n = n
        self.m = m
        self.first_row = None
        self.last_row = None
        self.next = None

    def add_row(self):
        """
        Adds a new row to the matrix.

        Returns:
            MatrixRow: The newly created MatrixRow object.

        If the matrix is empty, the new row will become both the first and last row.
        Otherwise, it will be appended to the end of the existing rows.
        """
        new_row = MatrixRow()
        if not self.first_row:
            self.first_row = new_row
            self.last_row = new_row
        else:
            self.last_row.next = new_row
            self.last_row = new_row
        return new_row

    def set_value(self, x, y, value):
        """
        Sets the value at a specific position in the matrix.

        Args:
            x (int): The row index where the value should be set.
            y (int): The column index where the value should be set.
            value (int): The value to be set at the specified position.

        If the row or column index is out of bounds, the value will not be set.
        """
        current_row = self.first_row
        for _ in range(x):
            if current_row is None:
                return
            current_row = current_row.next

        if current_row:
            new_node = MatrixNode(value)
            if current_row.head is None:
                current_row.head = new_node
                current_row.tail = new_node
            else:
                current_row.tail.next = new_node
                current_row.tail = new_node

    def get_value(self, x, y):
        """
        Retrieves the value at a specific position in the matrix.

        Args:
            x (int): The row index from which to retrieve the value.
            y (int): The column index from which to retrieve the value.

        Returns:
            int or None: The value at the specified position if found, otherwise None.

        If the row or column index is out of bounds, None is returned.
        """
        current_row = self.first_row
        for _ in range(x):
            if current_row is None:
                return None
            current_row = current_row.next

        if current_row:
            current_node = current_row.head
            for _ in range(y):
                if current_node is None:
                    return None
                current_node = current_node.next
            return current_node.value if current_node else None
