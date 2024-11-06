"""
This script defines custom exceptions and two classes: EmployeeInput and EmployeeOutput. These are used to manage and validate employee data for CRUD operations.

### Custom Exceptions:
1. **DuplicateEntryError**: Raised when trying to insert an employee with a duplicate entry (e.g., the same document).
2. **EntryNotFoundError**: Raised when an employee is not found in the database during a search or operation.
3. **DataValidationError**: Raised when input data is invalid (e.g., missing fields, invalid contract type, or incorrect salary format).

### EmployeeInput Class:
This class is used for handling input data related to an employee. It includes methods for validation and checking for duplicate entries in the database.

- `__init__(self, document, name, position, department, hire_date, contract_type, salary)`: Initializes the employee data attributes.
  
- `validate(self)`: Validates the employee's input data:
  - Checks if all fields are filled in.
  - Validates if the contract type is one of the allowed values: 'fijo_1_año', 'fijo_inferior_1_año', or 'indefinido'.
  - Validates if the salary is a positive number.

- `check_primary_key(document, db_check_func)`: This method checks if the employee's document already exists in the database by using an external function (`db_check_func`) that checks the database for duplicates. If a duplicate is found, it raises the `DuplicateEntryError`.

### EmployeeOutput Class:
This class is used for validating the output (retrieved employee data).

- `validate_employee_found(found, operation)`: This method checks if an employee was found in the database. If not, it raises an `EntryNotFoundError`. The error message indicates which operation (e.g., delete, update, or search) failed due to the employee not being found.

"""

import sys
sys.path.append("src")

class DuplicateEntryError(Exception):
    """Exception for duplicate entries in the database."""
    pass

class EntryNotFoundError(Exception):
    """Exception for searches where the entry does not exist in the database."""
    pass

class DataValidationError(Exception):
    """Exception for invalid input data."""
    pass

# EmployeeInput Class: Handles input data for employees, including validation
class EmployeeInput:
    def __init__(self, document, name, position, department, hire_date, contract_type, salary):
        self.document = document
        self.name = name
        self.position = position
        self.department = department
        self.hire_date = hire_date
        self.contract_type = contract_type
        self.salary = salary

    def validate(self):
        """
        Validates the input data for an employee.
        - Ensures all fields are provided.
        - Ensures the contract type is valid.
        - Ensures the salary is a positive number.
        """
        if not all([self.document, self.name, self.position, self.department, self.hire_date, self.contract_type, self.salary]):
            raise DataValidationError("All fields are required.")

        if self.contract_type not in ['fijo_1_año', 'fijo_inferior_1_año', 'indefinido']:
            raise DataValidationError("Invalid contract type. It must be 'fijo_1_año', 'fijo_inferior_1_año', or 'indefinido'.")

        if not isinstance(self.salary, (int, float)) or self.salary < 0:
            raise DataValidationError("Salary must be a positive number.")

    @staticmethod
    def check_primary_key(document, db_check_func):
        """
        Checks if the document already exists in the database.
        If the document exists, raises a DuplicateEntryError.
        :param document: The document ID of the employee.
        :param db_check_func: The database checking function that returns True if the document exists.
        """
        if db_check_func(document):
            raise DuplicateEntryError(f"An employee with document {document} already exists.")

# EmployeeOutput Class: Handles output data and validation for employee operations
class EmployeeOutput:
    @staticmethod
    def validate_employee_found(found, operation):
        """
        Validates whether the employee was found in the database.
        If not found, raises an EntryNotFoundError.
        :param found: A boolean indicating whether the employee was found.
        :param operation: The operation (e.g., delete, update) that was attempted.
        """
        if not found:
            raise EntryNotFoundError(f"Employee not found for operation: {operation}.")
