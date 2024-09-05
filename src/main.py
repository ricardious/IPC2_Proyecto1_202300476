import os

from src.utils.xml_parser import load_matrices_from_xml

BASE_DIR = r"C:\Users\T60\PycharmProjects\ IPC2_Proyecto1_202300476\data\input"


def display_menu():
    print("\n" + "-" * 40)
    print("               MAIN MENU")
    print("-" * 40)
    print(" [1] Load File")
    print(" [2] Process File")
    print(" [3] Write Output File")
    print(" [4] Show Student Info")
    print(" [5] Generate Graph")
    print(" [6] Exit")
    print("-" * 40)


def main():
    while True:
        display_menu()
        choice = input("Please choose an option (1-6): ")

        if choice == "1":
            file_path = input("Please enter the path of the XML file to load: ")
            file_path = os.path.join(BASE_DIR, file_path)
            matrices_list = load_matrices_from_xml(file_path)

            if matrices_list:
                print("Matrices loaded successfully.")

                current = matrices_list.head
                while True:
                    print(f"Matrix name: {current.name}")
                    print(f"Dimensions: {current.n}x{current.m}")
                    print("Matrix data:")
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
                print("No matrices could be loaded.")
        elif choice == "2":
            print("Process File selected.")
        elif choice == "3":
            print("Write Output File selected.")
        elif choice == "4":
            print("Name: Alex Ricardo Castañeda Rodríguez")
            print("Student ID: 202300476")
            print("Course: Introducción a la Programación y Computación 2 sección \"C\"")
            print("Major: Ingeniería en Ciencias y Sistemas")
            print("Semester: 4to")
        elif choice == "5":
            print("Generate Graph selected.")
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
