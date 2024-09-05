import sys
sys.path.append("src")

from Logic.employee import Employee

# Definition of custom exceptions
class EmployeeException(Exception):
    """Base class for exceptions related to the Employee class."""
    pass

class NegativeValueError(EmployeeException):
    """Exception for negative values."""
    def __init__(self, field, value):
        self.field = field
        self.value = value
        super().__init__(f"Error: The value '{value}' in the field '{field}' cannot be negative.")

class IncorrectDataTypeError(EmployeeException):
    """Exception for incorrect data types."""
    def __init__(self, field, expected_type, actual_type):
        self.field = field
        self.expected_type = expected_type
        self.actual_type = actual_type
        super().__init__(f"Error: The data type of the field '{field}' should be '{expected_type.__name__}' but received '{actual_type.__name__}'.")

class DivisionByZeroError(EmployeeException):
    """Exception for division by zero."""
    def __init__(self, message="Error: Division by zero detected."):
        super().__init__(message)

class NumberOutOfRangeError(EmployeeException):
    """Exception for numbers out of range."""
    def __init__(self, field, allowed_range, value):
        self.field = field
        self.allowed_range = allowed_range
        self.value = value
        super().__init__(f"Error: The value '{value}' in the field '{field}' is outside the allowed range {allowed_range}.")

class NonNumericValueError(EmployeeException):
    """Exception for non-numeric values."""
    def __init__(self, field, value):
        self.field = field
        self.value = value
        super().__init__(f"Error: The value '{value}' in the field '{field}' is not a valid number.")

def validate_input(field, value, expected_type):
    if not isinstance(value, expected_type):
        try:
            # Try converting to float to check if it's numeric
            float(value)
        except (ValueError, TypeError):
            raise NonNumericValueError(field, value)
        raise IncorrectDataTypeError(field, expected_type, type(value))
    if value < 0:
        raise NegativeValueError(field, value)

def verify_exceptions(employee):
    # Verifying data type and negative values
    validate_input("basic_salary", employee.basic_salary, (int, float))
    validate_input("one_twelfth_vacation_bonus", employee.one_twelfth_vacation_bonus, (int, float))
    validate_input("transportation_allowance", employee.transportation_allowance, (int, float))
    validate_input("worked_days", employee.worked_days, int)
    validate_input("severance_pay_for_accrued_leave_days", employee.severance_pay_for_accrued_leave_days, int)

    # Check possible divisions by zero
    if employee.DAYS_OF_THE_YEAR == 0:
        raise DivisionByZeroError("Error: 'DAYS_OF_THE_YEAR' cannot be zero.")
    if employee.HALF_A_SEMESTER_WORKED == 0:
        raise DivisionByZeroError("Error: 'HALF_A_SEMESTER_WORKED' cannot be zero.")
    if employee.DAYS_PER_MONTH == 0:
        raise DivisionByZeroError("Error: 'DAYS_PER_MONTH' cannot be zero.")

# Create an employee instance with test values
employee = Employee(
    basic_salary=877803,
    one_twelfth_vacation_bonus=0,
    transportation_allowance=102854,
    worked_days=200,
    severance_pay_for_accrued_leave_days=169,
)

# Function to calculate the severance pay amount
def calculate_severance_pay_amount(employee: Employee):
    severance_pay = round((employee.basic_salary + employee.one_twelfth_vacation_bonus + employee.transportation_allowance) / employee.DAYS_OF_THE_YEAR * employee.worked_days)
    return severance_pay

# Function to calculate the interest amount on severance pay
def calculate_severance_pay_interest(employee: Employee, severance_pay):
    severance_pay_interest = round((severance_pay * employee.MONTHS_OF_THE_YEAR) / employee.DAYS_OF_THE_YEAR * employee.worked_days)
    return severance_pay_interest

# Function to calculate the service bonus amount
def calculate_service_bonus(employee):
    service_bonus = round((employee.basic_salary + employee.one_twelfth_vacation_bonus + employee.transportation_allowance) / employee.HALF_A_SEMESTER_WORKED / employee.DAYS_WORKED_IN_THE_SEMESTER * employee.severance_pay_for_accrued_leave_days)
    return service_bonus

# Function to calculate vacation days
def calculate_vacation(employee):
    vacation = round((employee.basic_salary / employee.DAYS_PER_MONTH) * (employee.worked_days * employee.VACATION_PER_YEAR / employee.DAYS_OF_THE_YEAR))
    return vacation

# Function to calculate the vacation bonus amount
def calculate_vacation_bonus(employee):
    vacation_bonus = round((employee.basic_salary / employee.DAYS_PER_MONTH) * (employee.worked_days * employee.VACATION_PER_YEAR / employee.DAYS_OF_THE_YEAR))
    return vacation_bonus

# Function to calculate the final settlement amount
def calculate_liquidation(employee):
    verify_exceptions(employee)

    # Calcular todos los valores
    severance_pay = calculate_severance_pay_amount(employee)
    severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
    service_bonus = calculate_service_bonus(employee)
    vacation = calculate_vacation(employee)
    vacation_bonus = calculate_vacation_bonus(employee)

    # Retornar los resultados en un diccionario
    return {
        "severance_pay": severance_pay,
        "severance_pay_interest": severance_pay_interest,
        "service_bonus": service_bonus,
        "vacation": vacation,
        "vacation_bonus": vacation_bonus,
        "total_liquidation": severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
    }

"""
# Ejecutar la función con manejo de excepciones y obtener el retorno
try:
    results = calculate_liquidation(employee)
    print(results)  # Opcional, para ver los resultados
except EmployeeException as e:
    print(e)
"""