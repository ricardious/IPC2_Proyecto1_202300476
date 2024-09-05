import xml.etree.ElementTree as ET
from src.models.list import CircularLinkedList


def load_matrices_from_xml(file_path):
    """
    Loads matrices from an XML file and stores them in a CircularLinkedList.

    Args:
        file_path (str): The path to the XML file containing matrix data.

    Returns:
        CircularLinkedList: A CircularLinkedList containing Matrix objects loaded from the XML file.
        None: If there is an error loading the XML file.

    The XML file should have the following structure:
    <matrices>
        <matriz nombre="matrix_name" n="num_rows" m="num_columns">
            <dato x="row_index" y="column_index">value</dato>
            ...
        </matriz>
        ...
    </matrices>

    Each <matriz> element represents a matrix, and each <dato> element represents a data point within the matrix.
    The function creates a CircularLinkedList, appends each matrix to it, and sets the values in the matrices based on the XML data.
    """
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Initialize an empty circular linked list for storing matrices
        matrices_list = CircularLinkedList()

        # Iterate through each <matriz> element in the XML
        for matrix_element in root.findall('matriz'):
            matrix_name = matrix_element.get('nombre')
            n = int(matrix_element.get('n'))
            m = int(matrix_element.get('m'))

            # Append a new matrix to the circular linked list
            matrices_list.append(matrix_name, n, m)
            current_matrix = matrices_list.find_matrix(matrix_name)

            # Set the values in the matrix based on <dato> elements
            for data in matrix_element.findall('dato'):
                x = int(data.get('x')) - 1  # Convert to 0-based index
                y = int(data.get('y')) - 1  # Convert to 0-based index
                value = int(data.text)
                current_matrix.set_value(x, y, value)

        return matrices_list

    except Exception as e:
        print(f"Error loading XML file: {e}")
        return None
