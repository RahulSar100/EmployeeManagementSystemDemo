from logging import getLogger
from json import dump, load

class EmployeeSystem :
    def __init__(self) -> None:
        self._logger = getLogger(__name__)
        self._name = None
        self._ID = None
        self._department = None

    def add_employee(self, name:str, ID:str, department:str) :
        """
        Method to Add a Employee Record
        Input : 
            name - Employee Name
            ID - Employee ID
            department - department where employee belongs to
        Return :- None       
        """
        try :  
            self._logger.info("Setting up Employee data")
            self._name = name
            self._ID = ID
            self._department = department
            self._logger.info("Employee data is set.")
        except Exception as e :
            self._logger.error("Failed in add employee")
            raise RuntimeError("add employee failed")
        
    def get_employee_details(self) :
        """Method to get Employee details.
        Input :-
            None
        Return :- 
            A Tuple of 3 variables Employee Name, ID and department Name
        """ 
        if None in [self._name, self._ID, self._department] : 
            logger.error("One or more eemployee fields not set.")
            raise RuntimeError("Employee Details Not Set")
        return self._name, self._ID, self._department

    def display_employee_name_ID(self) :
        """Method to display employee name and ID in String format.
        Input :- 
            None
        Output :-
            str
        """ 
        if None in [self._name, self._ID, self._department] : 
            logger.error("One or more eemployee fields not set.")
            raise RuntimeError("Employee Details Not Set")
        return f"{self._name} - {self._ID}"

    def clear_employee_details(self) : 
        """Permanently removes the employee details from EmployeeSystem Class Instance."""
        logger.info("Performing Employee Data Cleanup")
        self._name = None
        self._ID = None
        self._department = None
        logger.info("Completed Employee Data Cleanup")
    
class DepartmentSystem :
    def __init__(self) -> None :
        self._department_name = None
        self._logger = logger
        # Array to store Employee details preserved as list of String
        self._employee_array = []

    def create_department(self, department_name:str) :
        """Method to Create a Department"""
        self._department_name = department_name

    def add_employee_to_department(employee : EmployeeSystem) :
        """Add a new employee record into the employee Array. Takes EmployeeSystem instance as Input"""
        try : 
            logger.info("Adding Employee into a Department.")
            employee_name, employee_ID, department_name = employee.get_employee_details()
            logger.info("Employee Name %s",employee_name, " Employee ID : %s",employee_ID, "Employee department Name : %s",department_name)
            self._employee_array.append({"Employee_Name" : employee_name,
            "Employee_ID" : employee_ID,
            "Department" : self._department_name})
            logger.info("Employee details Added")
        except Exception as e : 
            logger.error("Exception Raised : %s",str(e))
            raise RuntimeError("Error when Adding Employee to a Department")

    def delete_employee_from_department(employee_name:str) :
        """takes Employee Name and deletes the record from the employee Array"""
        try : 
            logger.info("Deleting Employee from Department")
            for emp in self._employee_array : 
                if emp.get("Employee_Name", None) == employee_name : 
                    self._employee_array.remove(emp)
                    logger.info("Employee Record Deleted")
                    return 1
            return 0
        except Exception as e : 
            logger.error("Exception Raised : %s",str(e))
            raise RuntimeError("Error when Deleting Employee to a Department")

    def list_all_employees() : 
        """This will Display all the Employee Data."""
        return self._employee_array

    def store_all_department_data() :
        """This will store the Employees Array into a JSON File""""
        with open("company_data.json", "w")  as data :
            dump(self._employee_array, data)
        logger.info("Data has been successfully stored in JSON FIle")
    
    def load_employee_data_from_json() :
        """This Method Loads Data from JSON File into the Employee Array"""
        with open("company_data.json", "r") as data :
            self._employee_array = load(data)


    
        

