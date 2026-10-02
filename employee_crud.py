import csv
import os


class Employee:
    file_name = "employees.csv"
    fields = ["id", "name", "department", "salary"]

    def create(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")

        file_exists = os.path.exists(self.file_name)

        with open(self.file_name, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "id": emp_id,
                "name": name,
                "department": department,
                "salary": salary
            })

        print("Employee added successfully.")


    def read(self):
        if not os.path.exists(self.file_name):
            print("No employee records found.")
            return

        with open(self.file_name, "r", newline="") as file:
            reader = csv.DictReader(file)

            print("\nEmployee Records")
            print("-" * 60)

            for employee in reader:
                print(
                    f"ID: {employee['id']} | "
                    f"Name: {employee['name']} | "
                    f"Department: {employee['department']} | "
                    f"Salary: {employee['salary']}"
                )


    def update(self):
        emp_id = input("Enter Employee ID to update: ")

        if not os.path.exists(self.file_name):
            print("No employee records found.")
            return

        employees = []

        with open(self.file_name, "r", newline="") as file:
            reader = csv.DictReader(file)

            for employee in reader:
                if employee["id"] == emp_id:
                    employee["name"] = input("Enter new name: ")
                    employee["department"] = input("Enter new department: ")
                    employee["salary"] = input("Enter new salary: ")
                    print("Employee updated successfully.")

                employees.append(employee)

        with open(self.file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(employees)


    def delete(self):
        emp_id = input("Enter Employee ID to delete: ")

        if not os.path.exists(self.file_name):
            print("No employee records found.")
            return

        employees = []
        found = False

        with open(self.file_name, "r", newline="") as file:
            reader = csv.DictReader(file)

            for employee in reader:
                if employee["id"] == emp_id:
                    found = True
                else:
                    employees.append(employee)

        with open(self.file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(employees)

        if found:
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")


def main():
    employee = Employee()

    while True:
        print("\n===== EMPLOYEE CRUD MENU =====")
        print("1. Create Employee")
        print("2. Read Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee.create()

        elif choice == "2":
            employee.read()

        elif choice == "3":
            employee.update()

        elif choice == "4":
            employee.delete()

        elif choice == "5":
            print("Program exited.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()