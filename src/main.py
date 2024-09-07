import os
from src.processing.data_processor import transform_to_binary_matrix, print_matrix, reduce_binary_matrix
from src.utils.xml_parser import load_matrices_from_xml
from src.utils.graphviz_helper import generate_graph

BASE_DIR = r"C:\Users\T60\PycharmProjects\ IPC2_Proyecto1_202300476\data\input"

# ANSI RGB escape sequences
MENU_COLOR = "\033[38;2;173;216;230m"  # Azul claro (RGB: 173, 216, 230)
EXIT_COLOR = "\033[38;2;255;99;71m"  # Rojo suave (RGB: 255, 99, 71)
INFO_COLOR = "\033[38;2;186;85;211m"  # Morado medio (RGB: 186, 85, 211)
RESET = "\033[0m"
cyan = "\033[38;2;0;255;255m"
teal = "\033[38;2;0;204;204m"
gray = "\033[38;2;0;153;153m"
reset = "\033[0m"

def print_custom_banner():
    print(f"{cyan}.S_sSSs     {teal}.S    sSSs   .S_SSSs     {gray}.S_sSSs     .S_sSSs     {teal}.S    sSSs_sSSs     {cyan}.S       S.     sSSs  {reset}")
    print(f"{cyan}.SS~YS%%b   {teal}.SS   d%%SP  .SS~SSSSS   {gray}.SS~YS%%b   .SS~YS%%b   {teal}.SS   d%%SP~YS%%b   {cyan}.SS       SS.   d%%SP  {reset}")
    print(f"{cyan}S%S   `S%b  {teal}S%S  d%S'    S%S   SSSS  {gray}S%S   `S%b  S%S   `S%b  {teal}S%S  d%S'     `S%b  {cyan}S%S       S%S  d%S'    {reset}")
    print(f"{cyan}S%S    S%S  {teal}S%S  S%S     S%S    S%S  {gray}S%S    S%S  S%S    S%S  {teal}S%S  S%S       S%S  {cyan}S%S       S%S  S%|     {reset}")
    print(f"{cyan}S%S    d*S  {teal}S&S  S&S     S%S SSSS%S  {gray}S%S    d*S  S%S    S&S  {teal}S&S  S&S       S&S  {cyan}S&S       S&S  S&S     {reset}")
    print(f"{cyan}S&S   .S*S  {teal}S&S  S&S     S&S  SSS%S  {gray}S&S   .S*S  S&S    S&S  {teal}S&S  S&S       S&S  {cyan}S&S       S&S  Y&Ss    {reset}")
    print(f"{cyan}S&S_sdSSS   {teal}S&S  S&S     S&S    S&S  {gray}S&S_sdSSS   S&S    S&S  {teal}S&S  S&S       S&S  {cyan}S&S       S&S  `S&&S   {reset}")
    print(f"{cyan}S&S~YSY%b   {teal}S&S  S&S     S&S    S&S  {gray}S&S~YSY%b   S&S    S&S  {teal}S&S  S&S       S&S  {cyan}S&S       S&S    `S*S  {reset}")
    print(f"{cyan}S*S   `S%b  {teal}S*S  S*b     S*S    S&S  {gray}S*S   `S%b  S*S    d*S  {teal}S*S  S*b       d*S  {cyan}S*b       d*S     l*S  {reset}")
    print(f"{cyan}S*S    S%S  {teal}S*S  S*S.    S*S    S*S  {gray}S*S    S%S  S*S   .S*S  {teal}S*S  S*S.     .S*S  {cyan}S*S.     .S*S    .S*P  {reset}")
    print(f"{cyan}S*S    S&S  {teal}S*S   SSSbs  S*S    S*S  {gray}S*S    S&S  S*S_sdSSS   {teal}S*S   SSSbs_sdSSS   {cyan}SSSbs_sdSSS   sSS*S   {reset}")
    print(f"{cyan}S*S    SSS  {teal}S*S    YSSP  SSS    S*S  {gray}S*S    SSS  SSS~YSSY    {teal}S*S    YSSP~YSSY    {cyan}YSSP~YSSY    YSS'    {reset}")
    print(f"{cyan}SP          {teal}SP                  SP   {gray}SP                      {teal}SP                      {cyan}       {reset}")
    print(f"{cyan}Y           {teal}Y                   Y    {gray}Y                       {teal}Y                       {cyan}       {reset}")
    print()


def display_menu():
    print("\n" + "-" * 40)
    print(f"{MENU_COLOR}               MAIN MENU{RESET}")
    print("-" * 40)
    print(f"{MENU_COLOR} [1] Load File{RESET}")
    print(f"{MENU_COLOR} [2] Process File{RESET}")
    print(f"{MENU_COLOR} [3] Write Output File{RESET}")
    print(f"{MENU_COLOR} [4] Show Student Info{RESET}")
    print(f"{MENU_COLOR} [5] Generate Graph{RESET}")
    print(f"{EXIT_COLOR} [6] Exit{RESET}")
    print("-" * 40)

def main():
    matrices_list = None
    print_custom_banner()
    while True:
        display_menu()
        choice = input(f"{MENU_COLOR}Please choose an option (1-6): {RESET}")

        if choice == "1":
            file_path = input(f"{MENU_COLOR}Please enter the path of the XML file to load: {RESET}")
            file_path = os.path.join(BASE_DIR, file_path)
            matrices_list = load_matrices_from_xml(file_path)

            if matrices_list:
                print(f"{MENU_COLOR}Matrices loaded successfully.{RESET}")

                current = matrices_list.head
                while True:
                    print(f"{MENU_COLOR}Matrix name: {current.name}{RESET}")
                    print(f"{MENU_COLOR}Dimensions: {current.n}x{current.m}{RESET}")
                    print(f"{MENU_COLOR}Matrix data:{RESET}")
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
                    if current == matrices_list.head:
                        break
            else:
                print(f"{EXIT_COLOR}No matrices could be loaded.{RESET}")
        elif choice == "2":
            if matrices_list is None:
                print(f"{EXIT_COLOR}No matrices to process. Please load a matrix first.{RESET}")
                continue

            matrix_name = input(f"{MENU_COLOR}Enter the name of the matrix to process: {RESET}")
            matrix = matrices_list.find_matrix(matrix_name)

            if matrix:
                print(f"{MENU_COLOR}Processing matrix...{RESET}")

                # Transform to binary matrix
                binary_matrix = transform_to_binary_matrix(matrix)
                print(f"{MENU_COLOR}Binary Matrix:{RESET}")
                print_matrix(binary_matrix)

                # Reduce binary matrix
                reduced_matrix = reduce_binary_matrix(binary_matrix, matrix)
                print(f"{MENU_COLOR}Reduced Matrix:{RESET}")
                print_matrix(reduced_matrix)
            else:
                print(f"{EXIT_COLOR}Matrix {matrix_name} not found.{RESET}")
        elif choice == "3":
            print(f"{MENU_COLOR}Write Output File selected.{RESET}")
        elif choice == "4":
            print(f"{INFO_COLOR}Name: Alex Ricardo Castañeda Rodríguez{RESET}")
            print(f"{INFO_COLOR}Student ID: 202300476{RESET}")
            print(f"{INFO_COLOR}Course: Introducción a la Programación y Computación 2 sección \"C\"{RESET}")
            print(f"{INFO_COLOR}Major: Ingeniería en Ciencias y Sistemas{RESET}")
            print(f"{INFO_COLOR}Semester: 4to{RESET}")
        elif choice == "5":
            if matrices_list is None:
                print(f"{EXIT_COLOR}No matrices to generate a graph. Please load a matrix first.{RESET}")
                continue

            print(f"{MENU_COLOR}Generate Graph selected.{RESET}")

            matrix_name = input(f"{MENU_COLOR}Enter the name of the matrix to generate a graph: {RESET}")
            matrix = matrices_list.find_matrix(matrix_name)

            if matrix:
                generate_graph(matrix)
            else:
                print(f"{EXIT_COLOR}Matrix {matrix_name} not found.{RESET}")
        elif choice == "6":
            print(f"{EXIT_COLOR}Exiting the program. Goodbye!{RESET}")
            break
        else:
            print(f"{EXIT_COLOR}Invalid option. Please select a number between 1 and 6.{RESET}")


if __name__ == "__main__":
    main()
