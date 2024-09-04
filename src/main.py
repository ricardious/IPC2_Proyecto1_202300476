def display_menu():
    print("\n" + "-"*40)
    print("               MAIN MENU")
    print("-"*40)
    print(" [1] Load File")
    print(" [2] Process File")
    print(" [3] Write Output File")
    print(" [4] Show Student Info")
    print(" [5] Generate Graph")
    print(" [6] Exit")
    print("-"*40)

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Please choose an option (1-6): ")

        if choice == "1":
            print("Load File selected.")
            # Logic for option 1 would go here
        elif choice == "2":
            print("Process File selected.")
            # Logic for option 2 would go here
        elif choice == "3":
            print("Write Output File selected.")
            # Logic for option 3 would go here
        elif choice == "4":
            print("Show Student Info selected.")
            # Logic for option 4 would go here
        elif choice == "5":
            print("Generate Graph selected.")
            # Logic for option 5 would go here
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 6.")