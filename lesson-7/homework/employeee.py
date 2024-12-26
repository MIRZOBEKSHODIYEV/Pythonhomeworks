class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.employee_id] = employee
        print("Employee added successfully!")

    def view_employees(self):
        if not self.employees:
            print("No employee records found.")
        else:
            print("Employee Records:")
            for emp in self.employees.values():
                print(emp)

    def search_employee(self, employee_id):
        employee = self.employees.get(employee_id)
        if employee:
            print("Employee Found:")
            print(employee)
        else:
            print("Employee not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        employee = self.employees.get(employee_id)
        if employee:
            if name: employee.name = name
            if position: employee.position = position
            if salary: employee.salary = salary
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    def delete_employee(self, employee_id):
        if self.employees.pop(employee_id, None):
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

# Main program
if __name__ == "__main__":
    manager = EmployeeManager()

    while True:
        print("\nWelcome to the Employee Records Manager!")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            employee = Employee(employee_id, name, position, salary)
            manager.add_employee(employee)
        elif choice == "2":
            manager.view_employees()
        elif choice == "3":
            employee_id = input("Enter Employee ID to search: ")
            manager.search_employee(employee_id)
        elif choice == "4":
            employee_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (leave blank to skip): ") or None
            position = input("Enter new Position (leave blank to skip): ") or None
            salary = input("Enter new Salary (leave blank to skip): ") or None
            manager.update_employee(employee_id, name, position, salary)
        elif choice == "5":
            employee_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(employee_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
