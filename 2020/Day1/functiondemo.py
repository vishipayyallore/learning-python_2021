# Variables with Global Scope
name = 'XXX'
employee_id = 0
salary = 0.0
is_manager = False

def get_employee_details():
    print("Starting the Function")
    name = input('Enter your name: ') # Creating the Local Variable
    print(f"Local Name: {name}") 

print("Starting the Program")
get_employee_details() # Invoking the function

print(f"Name: {name}")


