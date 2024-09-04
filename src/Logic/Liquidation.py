import sys
sys.path.append("Logic")

from employee import Employee

# Definición de excepciones personalizadas
class EmployeeException(Exception):
    """Clase base para excepciones relacionadas con la clase Employee."""
    pass

class NegativeValue(EmployeeException):
    """Exception for negative values."""
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value
        super().__init__(f"Error: El valor '{value}' en el campo '{variable}' no puede ser negativo.")

class IncorrectDataType(EmployeeException):  
    """Exception for incorrect data types."""  
    def __init__(self, variable, expected_type, actual_type):  
        self.variable = variable  
        self.expected_type = expected_type  
        self.actual_type = actual_type  
        super().__init__(f"Error: El tipo de dato del campo '{variable}' debería ser '{expected_type.__name__}' pero se recibió '{actual_type.__name__}'.")

class DivisionByZero(EmployeeException):  
    """Exception for division by zero."""  
    def __init__(self, message="Error: Division por cero detectada."):  
        super().__init__(message)

class NumberOutOfRange(EmployeeException):  
    """Exception for numbers out of range."""  
    def __init__(self, variable, allowed_range, value):  
        self.variable = variable  
        self.allowed_range = allowed_range  
        self.value = value  
        super().__init__(f"Error: El valor '{value}' en el campo '{variable}' está fuera del rango permitido {allowed_range}.")

# Function to validate input values  
def validate_input(variable, value, expected_type):  
    if not isinstance(value, expected_type):  
        raise IncorrectDataType(variable, expected_type, type(value))  
    if value < 0:  
        raise NegativeValue(variable, value)
    
        # Function that validates the exceptions
def verify_exceptions(employee):
    # Verifying data type and negative values
    validate_input("basic_salary", employee.basic_salary, (int, float))
    validate_input("one_twelfth_vacation_bonus", employee.one_twelfth_vacation_bonus, (int, float))
    validate_input("transportation_allowance", employee.transportation_allowance, (int, float))
    validate_input("worked_days", employee.worked_days, int)
    validate_input("severance_pay_for_accrued_leave_days", employee.severance_pay_for_accrued_leave_days, int)

    # Check possible divisions by zero
    if employee.int_DAYS_OF_THE_YEAR == 0:
        raise DivisionByZero("Error: 'int_DAYS_OF_THE_YEAR' no puede ser cero.")
    if employee.int_HALF_A_SEMESTER_WORKED == 0:
        raise DivisionByZero("Error: 'int_HALF_A_SEMESTER_WORKED' no puede ser cero.")
    if employee.int_DAYS_PER_MONTH == 0:
        raise DivisionByZero("Error: 'int_DAYS_PER_MONTH' no puede ser cero.")

# Crear una instancia deEmployee con valuees de prueba
employee = Employee(
    basic_salary=877803,
    one_twelfth_vacation_bonus=0,
    transportation_allowance=102854,
    worked_days=200,
    severance_pay_for_accrued_leave_days=169,
)

# Validate inputs to avoid exceptions  
try:  
    validate_input("basic_salary", employee.basic_salary, (int, float))  
    validate_input("one_twelfth_vacation_bonus", employee.one_twelfth_vacation_bonus, (int, float))  
    validate_input("transportation_allowance", employee.transportation_allowance, (int, float))  
    validate_input("worked_days", employee.worked_days, int)  
    validate_input("severance_pay_for_accrued_leave_days", employee.severance_pay_for_accrued_leave_days, int)

    def calculate_severance_pay_interest_amount(employee):
        if employee.int_DAYS_OF_THE_YEAR == 0:
            raise DivisionByZero("Error: 'int_DAYS_OF_THE_YEAR' no puede ser cero.")
        severance_pay = round((employee.basic_salary + employee.one_twelfth_vacation_bonus + employee.transportation_allowance) /employee.int_DAYS_OF_THE_YEAR *employee.worked_days)
        return severance_pay

    def calculate_severance_pay_interest(employee, severance_pay):
        if employee.int_DAYS_OF_THE_YEAR == 0:
            raise DivisionByZero("Error: 'int_DAYS_OF_THE_YEAR' no puede ser cero.")
        severance_pay_interest = round((severance_pay *employee.int_MONTHS_OF_THE_YEAR ) /employee.int_DAYS_OF_THE_YEAR * employee.worked_days)
        return severance_pay_interest

    def calculate_service_bonus(employee):
        if employee.int_HALF_A_SEMESTER_WORKED == 0:
            raise DivisionByZero("Error: 'HALF_A_SEMESTER_WORKED' no puede ser cero.")
        service_bonus = round((employee.basic_salary + employee.one_twelfth_vacation_bonus + employee.transportation_allowance) /employee.int_HALF_A_SEMESTER_WORKED /employee.int_DAYS_WORKED_IN_THE_SEMESTER * employee.severance_pay_for_accrued_leave_days)
        return service_bonus

    def calcute_vacation(employee):
        if employee.int_DAYS_PER_MONTH == 0:
            raise DivisionByZero("Error: 'int_DAYS_PER_MONTH' no puede ser cero.")
        vacation = round((employee.basic_salary /employee.int_DAYS_PER_MONTH) * (employee.worked_days * employee.int_VACATION_PER_YEAR /employee.int_DAYS_OF_THE_YEAR))
        return vacation

    def calculate_vacation_bonus(employee):
        if employee.int_DAYS_PER_MONTH == 0:
            raise DivisionByZero("Error: 'int_DAYS_PER_MONTH' no puede ser cero.")
        vacation_bonus = round((employee.basic_salary /employee.int_DAYS_PER_MONTH) * (employee.worked_days * employee.int_VACATION_PER_YEAR /employee.int_DAYS_OF_THE_YEAR))
        return vacation_bonus

    # Calculate all the values
    severance_pay = calculate_severance_pay_interest(employee)
    severance_pay_interest = calculate_severance_pay_interest_amount(employee, severance_pay)
    service_bonus = calculate_service_bonus(employee)
    vacation = calcute_vacation(employee)
    vacation_bonus = calculate_vacation_bonus(employee)

    # Print the results
    print(f"Cesantías: {severance_pay}")
    print(f"severance_pay_interest: {severance_pay_interest}")
    print(f"Prima de servicios: {service_bonus}")
    print(f"vacationes: {vacation}")
    print(f"Prima de vacationes: {vacation_bonus}")

    # calculate la liquidación total
    liquidacion = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus

    # Imprimir la liquidación calculada
    print(f"La liquidación calculada: {liquidacion}")

except EmployeeException as e:
    print(e)
