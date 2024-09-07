from src.models.list import CircularLinkedList
from src.models.node import MatrixRow
from src.models.pattern_list import PatternList


def transform_to_binary_matrix(matrix):
    binary_matrix = CircularLinkedList()
    current_row = matrix.first_row

    while current_row:
        binary_row = MatrixRow()
        current_node = current_row.head
        col_index = 0
        while current_node:
            value = 1 if current_node.value > 0 else 0
            binary_row.add_value(col_index, value)
            current_node = current_node.next
            col_index += 1
        binary_matrix.append("", 1, matrix.m)
        binary_matrix.find_matrix("").add_row(binary_row)
        current_row = current_row.next

    return binary_matrix


def reduce_binary_matrix(binary_matrix, original_matrix):
    reduced_matrix = CircularLinkedList()
    seen_patterns = PatternList()
    current = binary_matrix.head

    while current:
        print("Processing binary matrix node...")
        # Generar el patrón de la fila actual
        pattern = ""
        current_row = current.first_row
        while current_row:
            current_node = current_row.head
            while current_node:
                pattern += str(current_node.value)
                current_node = current_node.next
            current_row = current_row.next

        print(f"Generated pattern: {pattern}")

        if not pattern:
            print("Empty pattern, skipping...")
            current = current.next
            if current == binary_matrix.head:
                break
            continue

        pattern_index = seen_patterns.find_pattern(pattern)
        if pattern_index is None:
            pattern_index = seen_patterns.add_pattern(pattern)
            reduced_matrix.append(f"Reduced_{pattern_index}", original_matrix.n, original_matrix.m)
            print(f"Added new matrix for pattern {pattern_index}")

        reduced_matrix_instance = reduced_matrix.find_matrix(f"Reduced_{pattern_index}")
        if reduced_matrix_instance:
            reduced_matrix_row = reduced_matrix_instance.first_row
            if not reduced_matrix_row:
                reduced_matrix_row = MatrixRow()
                reduced_matrix_instance.add_row(reduced_matrix_row)
                print(f"Added new row to matrix for pattern {pattern_index}")
        else:
            print(f"Matrix for pattern {pattern_index} not found!")
            current = current.next
            if current == binary_matrix.head:
                break
            continue

        original_row = original_matrix.first_row
        while original_row:
            original_pattern = ""
            original_node = original_row.head
            while original_node:
                original_pattern += str(1 if original_node.value > 0 else 0)
                original_node = original_node.next

            print(f"Original pattern: {original_pattern}")

            if original_pattern == pattern:
                print(f"Adding values for original pattern: {original_pattern}")
                reduced_matrix_row = reduced_matrix_instance.first_row
                if not reduced_matrix_row:
                    reduced_matrix_row = MatrixRow()
                    reduced_matrix_instance.add_row(reduced_matrix_row)
                    print(f"Added new row to reduced matrix for pattern {pattern_index}")

                original_row_node = original_row.head
                while original_row_node:
                    reduced_matrix_row_node = reduced_matrix_row.head
                    if not reduced_matrix_row_node:
                        reduced_matrix_row_node = MatrixRow()
                        reduced_matrix_row.add_row(reduced_matrix_row_node)
                    while original_row_node:
                        if reduced_matrix_row_node is None:
                            reduced_matrix_row_node = MatrixRow()
                            reduced_matrix_row.add_row(reduced_matrix_row_node)
                        reduced_matrix_row_node.value += original_row_node.value
                        reduced_matrix_row_node = reduced_matrix_row_node.next
                        original_row_node = original_row_node.next

            original_row = original_row.next

        current = current.next
        if current == binary_matrix.head:
            break

    # Print the reduced matrix
    print("Reduced Matrix:")
    print_matrix(reduced_matrix)

    return reduced_matrix


def print_matrix(matrix):
    current = matrix.head
    while True:
        print(f"Matrix name: {current.name}")
        print(f"Dimensions: {current.n}x{current.m}")
        current_row = current.first_row
        row_index = 0
        while current_row:
            current_node = current_row.head
            col_index = 0
            while current_node:
                print(f"({row_index}, {col_index}): {current_node.value}", end=" ")
                current_node = current_node.next
                col_index += 1
            print()
            current_row = current_row.next
            row_index += 1
        print()
        current = current.next
        if current == matrix.head:
            break


def print_matrix(matrix):
    current = matrix.head
    if not current:
        print("The matrix is empty.")
        return

    start = current

    while True:

        current_row = current.first_row
        row_index = 0
        while current_row:
            current_node = current_row.head
            col_index = 0
            row_str = ""
            while current_node:
                row_str += f"({row_index + 1}, {col_index}): {current_node.value}  "
                current_node = current_node.next
                col_index += 1
            print(row_str)
            current_row = current_row.next
            row_index += 1

        print()

        current = current.next
        if current == start:
            break
