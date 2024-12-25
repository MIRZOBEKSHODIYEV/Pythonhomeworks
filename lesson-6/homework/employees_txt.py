def create_or_open_file(filename):
    
    try:
        with open(filename, 'a') as file:
            pass
    except IOError as e:
        print(f"Error creating or opening file: {e}")

def add_employee_record_simple(filename):
    
    try:
        with open(filename, 'a') as file:
            employee_id = input("ID: ")
            name = input("Name: ")
            position = input("Position: ")
            salary = input("Salary: ")

            file.write(f"{employee_id}, {name}, {position}, {salary}\n")
            print("Record added.")
    except IOError as e:
        print(f"Error writing to file: {e}")

def main_simple():
    filename = "employees.txt"
    create_or_open_file(filename)

    while True:
        choice = input("Add record (yes/no)? ")

        if choice.lower() == 'yes':
            add_employee_record_simple(filename)
        elif choice.lower() == 'no':
            print("Thats all.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main_simple()
