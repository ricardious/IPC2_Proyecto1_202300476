from src.models.node import Matrix


class CircularLinkedList:
    """
    A class to represent a circular linked list of Matrix objects.
    """

    def __init__(self):
        """
        Initializes an empty circular linked list.
        """
        self.head = None

    def append(self, name, n, m):
        """
        Appends a new Matrix to the circular linked list.

        Args:
            name (str): The name of the new Matrix.
            n (int): The number of rows for the new Matrix.
            m (int): The number of columns for the new Matrix.

        The new Matrix will be appended to the end of the list and will point to the head of the list,
        making it circular.
        """
        new_matrix = Matrix(name, n, m)

        # Add rows to the new matrix
        for _ in range(n):
            new_matrix.add_row()

        if not self.head:
            # If the list is empty, set the new matrix as the head and point to itself
            self.head = new_matrix
            self.head.next = self.head
        else:
            # Traverse the list to find the last matrix
            current = self.head
            while current.next != self.head:
                current = current.next
            # Append the new matrix to the end of the list
            current.next = new_matrix
            new_matrix.next = self.head

    def find_matrix(self, name):
        """
        Finds a Matrix in the circular linked list by its name.

        Args:
            name (str): The name of the Matrix to find.

        Returns:
            Matrix: The Matrix object with the specified name if found, otherwise None.

        This method traverses the circular linked list to find the Matrix with the matching name.
        If the name is not found after one full traversal, None is returned.
        """
        if not self.head:
            return None

        current = self.head
        while True:
            if current.name == name:
                return current
            current = current.next
            if current == self.head:
                break
        return None
