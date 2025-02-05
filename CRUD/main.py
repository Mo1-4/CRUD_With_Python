## Program - CRUD

employees = []

def createEmployee():
    name = input("Enter The Employee Name: ").strip().capitalize()
    age = int(input("Enter The Employee Age: ").strip())
    position = input("Enter The Employee Position: ").strip().capitalize()
    employees.append({"name": name, "age": age, "position": position})
    print("=" * 30)
    print(f"{name} has been added")
    print("=" * 30)


def readEmployee():
    checkName = input("Enter the name of the employee: ").strip().capitalize()
    found = False
    for employee in employees:
        if employee["name"] == checkName:
            print("=" * 30)
            print(f"Name: {employee['name']}")
            print(f"Age: {employee['age']}")
            print(f"Position: {employee['position']}")
            print("=" * 30)
            found = True
    if found == False:
        print("=" * 30)
        print("Employee not found")
        print("=" * 30)



def updateEmployee():
    name = input("Enter the name of the employee: ").strip().capitalize()
    found = False
    for employee in employees:
        if employee["name"] == name:
            employee["name"] = input("Enter the new name of the employee: ").strip().capitalize()
            employee["age"] = int(input("Enter the new age of the employee: ").strip())
            employee["position"] = input("Enter the new position of the employee: ").strip().capitalize()
            print("=" * 30)
            print(f"{employee["name"]} has been updated")
            print("=" * 30)
            found = True

    if found == False:
        print("=" * 30)
        print("Employee not found")
        print("=" * 30)

def deleteEmployee():
    name = input("Enter the name of the employee: ").strip().capitalize()
    found = False
    for employee in employees:
        if employee["name"] == name:
            employees.remove(employee)
            print("=" * 30)
            print(f"{employee["name"]} has been deleted")
            print("=" * 30)
            found = True

    if found == False:
        print("=" * 30)
        print("Employee not found")
        print("=" * 30)


option = input("Welcome to the database \n Do you want to create an employee? (Y/N): ").strip().capitalize()
if option == "Y":
        createEmployee()
        continueOption = input(f"Do you want to continue into the database settings? (Y/N): ").strip().capitalize()
        while True:
            if continueOption == "Y":
                print("1. Read Employee")
                print("2. Update Employee")
                print("3. Delete Employee")
                print("4. Create Employee")
                print("5. Exit")

                options = int(input("Enter the number of the option you want to use: ").strip())

                if options == 1:
                    readEmployee()
                elif options == 2:
                    updateEmployee()
                elif options == 3:
                    deleteEmployee()
                elif options == 4:
                    createEmployee()
                elif options == 5:
                    print("Thank you for using the database (:")
                    break
                else:
                    print("Invalid option")
                    break

            elif option == "N":
                print("Thank you for using the database (:")
                break
            else:
                print("Invalid option")
                break

        
else:
        while True:
            options = input("Do you want to continue into the database settings? (Y/N): ").strip().capitalize()

            if options == "Y":
                print("1. Read Employee")
                print("2. Update Employee")
                print("3. Delete Employee")
                print("4. Create Employee")
                print("5. Exit")
                options = int(input("Enter the number of the option you want to use: ").strip())

                if options == 1:
                    readEmployee()
                elif options == 2:
                    updateEmployee()
                elif options == 3:
                    deleteEmployee()
                elif options == 4:
                    createEmployee()
                elif options == 5:
                    print("Thank you for using the database (:")
                    break
                else:
                    print("Invalid option")
                    break

            elif options == "N":
                print("Thank you for using the database (:")
                break
            else:
                print("Invalid option")
                break