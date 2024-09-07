import graphviz


def generate_graph(matrix):
    dot = graphviz.Digraph(comment=matrix.name)

    # Nodo para el nombre de la matrix (por ejemplo, "Ejemplo")
    dot.node('Ejemplo', f'{matrix.name}', shape='ellipse')

    # Nodos separados para 'n' y 'm' directamente desde el nombre de la matriz
    dot.node('N', f'n = {matrix.n}', shape='circle', style='bold', color='yellow', penwidth='3')
    dot.node('M_', f'm = {matrix.m}', shape='circle', style='bold', color='yellow', penwidth='3')

    # Conectar 'n' y 'm' con el nodo del nombre de la matrix
    dot.edge('Ejemplo', 'N', constraint='false')
    dot.edge('Ejemplo', 'M_', constraint='false')

    # Graficar cada dato de la matrix directamente sin mostrar posiciones
    current_row = matrix.first_row
    row_index = 0
    while current_row:
        current_node = current_row.head
        col_index = 0
        while current_node:
            # Solo mostrar el valor, sin posiciones
            dot.node(f'{row_index}_{col_index}', f'{current_node.value}', shape='ellipse')

            if row_index == 0:  # Conectar los elementos de la primera fila a "Ejemplo"
                dot.edge('Ejemplo', f'{row_index}_{col_index}')
            else:  # Conectar los elementos de las filas entre sí
                dot.edge(f'{row_index-1}_{col_index}', f'{row_index}_{col_index}')

            current_node = current_node.next
            col_index += 1
        row_index += 1
        current_row = current_row.next

    # Save the generated graph as a PNG file
    dot.render(f'matrix_graph_{matrix.name}', format='png', cleanup=True)
    print(f"Graph generated as matrix_graph_{matrix.name}.png")