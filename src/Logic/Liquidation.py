import sys
sys.path.append("src")

from Logic.employee import Employee

from decimal import Decimal, ROUND_HALF_UP

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
            # Intentar convertir el valor a float para ver si es numérico
            float(value)
        except (ValueError, TypeError):
            # Si la conversión falla, es un valor no numérico
            raise NonNumericValueError(field, value)
        # Si se convierte correctamente a float, lanzar excepción de tipo incorrecto
        raise IncorrectDataTypeError(field, expected_type, type(value))
    # Verificar si el valor es negativo
    if value < 0:
        raise NegativeValueError(field, value)


def verify_exceptions(employee):
    # Verificando tipo de datos y valores negativos
    validate_input("basic_monthly_salary", employee.basic_monthly_salary, (int, float))
    validate_input("transportation_allowance", employee.transportation_allowance, (int, float))
    validate_input("worked_days", employee.worked_days, int)
    validate_input("severance_pay_for_accrued_leave_days", employee.severance_pay_for_accrued_leave_days, int)

def verify_constants():
    # Validando constantes para asegurar que no hay divisiones por cero
    if DAYS_OF_THE_YEAR == 0:
        raise DivisionByZeroError("Error: 'DAYS_OF_THE_YEAR' cannot be zero.")
    if HALF_A_SEMESTER_WORKED == 0:
        raise DivisionByZeroError("Error: 'HALF_A_SEMESTER_WORKED' cannot be zero.")
    if DAYS_PER_MONTH == 0:
        raise DivisionByZeroError("Error: 'DAYS_PER_MONTH' cannot be zero.")

# Constantes para los cálculos
PERCENTAGE_OF_SEVERANCE_PAY = 0.12 
MONTHS_OF_THE_YEAR = 12
DAYS_OF_THE_YEAR = 360 
VACATION_PER_YEAR = 15
DAYS_PER_MONTH = 30
HALF_A_SEMESTER_WORKED = 2 
DAYS_WORKED_IN_THE_SEMESTER = 180 
TOTAL_SEMIANNUAL_PREMIUM_INSTALLMENTS = 0.6 
HOUR_WORKED_IN_A_SEMESTER = 720

# Function to calculate the severance pay amount
def calculate_severance_pay_amount(employee: Employee):
    severance_pay = ((employee.average_salary * employee.worked_days) / DAYS_OF_THE_YEAR)
    return severance_pay

# Function to calculate the interest amount on severance pay
def calculate_severance_pay_interest(employee: Employee, severance_pay):
    severance_pay_interest = ((severance_pay * employee.worked_days * PERCENTAGE_OF_SEVERANCE_PAY) / DAYS_OF_THE_YEAR)
    return severance_pay_interest

# Function to calculate the service bonus amount
def calculate_service_bonus(employee: Employee):
    service_bonus = ((employee.average_salary * employee.worked_days) / DAYS_OF_THE_YEAR)
    return service_bonus

# Function to calculate vacation days
def calculate_vacation(employee: Employee):
    vacation = ((employee.basic_monthly_salary * employee.worked_days) / HOUR_WORKED_IN_A_SEMESTER)
    return vacation

# Function to calculate the final settlement amount
def calculate_liquidation(employee):
    # Validar el objeto empleado
    verify_exceptions(employee)
    
    # Validar las constantes antes de los cálculos
    verify_constants()

    # Calcular todos los valores
    severance_pay = calculate_severance_pay_amount(employee)
    severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
    service_bonus = calculate_service_bonus(employee)
    vacation = calculate_vacation(employee)
    total_liquidation = round(severance_pay + severance_pay_interest + service_bonus + vacation)
    
    # Retornar los resultados en un diccionario
    return {
        "severance_pay": severance_pay,
        "severance_pay_interest": severance_pay_interest,
        "service_bonus": service_bonus,
        "vacation": vacation,
        "total_liquidation": total_liquidation
    }
