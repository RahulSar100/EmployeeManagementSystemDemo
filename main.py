from ems import EmployeeSystem, DepartmentSystem
from logger import getLogger

logger = getLogger(__name__)

# making these variables as global as will be used in many methods.
emp_system = EmployeeSystem()
dept_system = DepartmentSystem()


def create_employee() : 
    logger.info("Creating a New Employee")
    name = input("Employee Name : ")
    emp_id = input("Employee ID : ")
    # passing empty string as at this stage only employee data is created but not assigned to a department
    department = ""
    emp_system.add_employee(name,emp_id, department)
    logger.info("Employee Data Added")

def clear_employee_data() : 
    emp_system.clear_employee_data()

def display_employee_data() : 
    logger.info(emp_system.display_employee_name_ID())

def create_new_department() :
    dept_name = input("What will be the department Name?") 
    logger.info("Initiate Department Creation.")
    dept_system.create_department(dept_name)

def add_employee_to_department() : 
    if dept_system.department_name is None : 
        logger.error("Please create a Department first before adding Employees to a Department.")
        raise RuntimeError("Department Data is not Set")
    if emp_system.employee_name is None : 
        logger.error("Please insert the Employee Data into the Employee Management system first")
        raise RuntimeError("Employee Data is not Set.")
    logger.info("Adding Employee to the Department.")
    dept_system.add_employee_to_department(emp_system)
    logger.info("Operation Done")

def delete_employee_from_department_operation() :
    if dept_system.department_name is None : 
        logger.error("Please create a Department first before adding Employees to a Department.")
    raise RuntimeError("Department Data is not Set")
    emp_name = input("Name of the Employee to be deleted from the Department")
    result = dept_system.delete_employee_from_department(emp_name)
    if result == 0 : 
        logger.info("No Employee Data was deleted")
    elif result == 1 : 
        logger.info("Employee Data deleted successfully.")

def display_all_employees_from_department() : 
    dept_data = dept_system.list_all_employees()
    if len(dept_data) > 0 :
        logger.info("Department has no Employees assigned to them.")
    else : 
        for row in dept_data : 
            logger.info(f"Employee Name : {row.get("Employee_Name","")} | Employee_ID : {row.get("employee_ID")}")



def list_operations() : 
    print("Welcome to Employee Management System.", 
    "\n1. Create new Employee.",
    "\n2. Display Employee Details.",
    "\n3. Remove Employee Details.",
    "\n4. Create a New Department.",
    "\n5. Add Employee to a Department.",
    "\n6. Remove Employee from a Department.",
    "\n7. Display all Employees from a Department.",
    "\n8. Export Data to JSON",
    "\n9. Import Data into JSON")
    # Using Python Dictionary as switch case like in C, Java
    return  dict(
        "1" = create_employee(), 
        "2" = display_employee_data(),
        "3" = clear_employee_data(),
        "4" = create_new_department(),
        "5" = add_employee_to_department(),
        "6" = delete_employee_from_department_operation(),
        "7" = display_all_employees_from_department(),
        "8" = dept_system.store_all_department_data(),
        "9" = dept_data.load_employee_data_from_json()
    )
    


if __name__ == "__main__" : 
    list_operations()
    input_opr = Input("Plese select the Appropriate Number for the Operation.")
    operations = list_operations()
    #This will Invote the function assigned to the operation.
    operations.get(input_opr)

    


