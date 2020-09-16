# Variables with Global Scope
name = ''
age = 0
salary = 0.0
is_manager = False

def get_employee_details():
    # using global variables
    global name, age, salary, is_manager

    print("Starting the Function")
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    salary = float(input('Enter your Salary: '))
    is_manager = bool(int(input("Enter Manager Status (0/1): ")))

def show_employee_details():
    print("====================================================")
    print("***************** Employee Details *****************")
    print("====================================================")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Salary: {salary}")
    print(f"Is Manager: {is_manager}")
    print("----------------------------------------------------")

def main():
    print("Starting the Program")
    get_employee_details() # Invoking the function
    show_employee_details() # Invoking the function


# Program execution starts here
main()