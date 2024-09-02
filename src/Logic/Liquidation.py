import sys
sys.path.append("Logic")

from Employee import Employee

# Definición de excepciones personalizadas
class EmployeeException(Exception):
    """Clase base para excepciones relacionadas con la claseEmployee."""
    pass

class NegativeValue(EmployeeException):
    """Exception for negative values."""
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value
        super().__init__(f"Error: El value '{value}' en el variable '{variable}' no puede ser negativo.")

class IncorrectDataType(EmployeeException):  
    """Exception for incorrect data types."""  
    def __init__(self, variable, expected_type, actual_type):  
        self.variable = variable  
        self.expected_type = expected_type  
        self.actual_type = actual_type  
        super().__init__(f"Error: The data type of variable '{variable}' should be '{expected_type.__name__}' but received '{actual_type.__name__}'.")

class DivisionByZero(EmployeeException):  
    """Exception for division by zero."""  
    def __init__(self, message="Error: Division by zero detected."):  
        super().__init__(message)

class NumberOutOfRange(EmployeeException):  
    """Exception for numbers out of range."""  
    def __init__(self, variable, allowed_range, value):  
        self.variable = variable  
        self.allowed_range = allowed_range  
        self.value = value  
        super().__init__(f"Error: The value '{value}' for variable '{variable}' is out of the allowed range {allowed_range}.")

# Function to validate input values  
def validate_input(variable, value, expected_type):  
    if not isinstance(value, expected_type):  
        raise IncorrectDataType(variable, expected_type, type(value))  
    if value < 0:  
        raise NegativeValue(variable, value)

# Crear una instancia deEmployee con valuees de prueba
Employee = Employee(
    basic_salary=877803,
    one_twelfth_vacation_bonus=0,
    transportation_allowance=102854,
    worked_days=200,
    severance_pay_for_accrued_leave_days=169,
)

# Validate inputs to avoid exceptions  
try:  
    validate_input("basic_salary", Employee.basic_salary, (int, float))  
    validate_input("one_twelfth_vacation_bonus", Employee.one_twelfth_vacation_bonus, (int, float))  
    validate_input("transportation_allowance", Employee.transportation_allowance, (int, float))  
    validate_input("worked_days", Employee.worked_days, int)  
    validate_input("severance_pay_for_accrued_leave_days", Employee.severance_pay_for_accrued_leave_days, int)

    def calculate_severance_pay_interest(Employee:Employee):
        if Employee.int_DAYS_OF_THE_YEAR == 0:
            raise DivisionByZero("Error: 'int_DAYS_OF_THE_YEAR' no puede ser cero.")
        severance_pay = round((Employee.basic_salary + Employee.one_twelfth_vacation_bonus +Employee.transportation_allowance) /Employee.int_DAYS_OF_THE_YEAR *Employee.worked_days)
        return severance_pay

    def severance_pay_interest(Employee:Employee, severance_pay):
        if Employee.int_DAYS_OF_THE_YEAR == 0:
            raise DivisionByZero("Error: 'int_DAYS_OF_THE_YEAR' no puede ser cero.")
        severance_pay_interest = round((severance_pay *Employee.int_MONTHS_OF_THE_YEAR ) /Employee.int_DAYS_OF_THE_YEAR *Employee.worked_days)
        return severance_pay_interest

    def calculate_service_bonus(Employee: Employee):
        if Employee.HALF_A_SEMESTER_WORKED == 0:
            raise DivisionByZero("Error: 'HALF_A_SEMESTER_WORKED' no puede ser cero.")
        service_bonus = round((Employee.basic_salary +Employee.one_twelfth_vacation_bonus +Employee.transportation_allowance) /Employee.HALF_A_SEMESTER_WORKED /Employee.int_DAYS_WORKED_IN_THE_SEMESTER *Employee.severance_pay_for_accrued_leave_days)
        return service_bonus

    def vacation(Employee:Employee):
        if Employee.int_DAYS_PER_MONTH == 0:
            raise DivisionByZero("Error: 'int_DAYS_PER_MONTH' no puede ser cero.")
        vacation = round((Employee.basic_salary /Employee.int_DAYS_PER_MONTH) * (Employee.worked_days *Employee.int_VACATION_PER_YEAR /Employee.int_DAYS_OF_THE_YEAR))
        return vacation

    def calculate_vacation_bonus(Employee:Employee):
        if Employee.int_DAYS_PER_MONTH == 0:
            raise DivisionByZero("Error: 'int_DAYS_PER_MONTH' no puede ser cero.")
        vacation_bonus = round((Employee.basic_salary /Employee.int_DAYS_PER_MONTH) * (Employee.worked_days *Employee.int_VACATION_PER_YEAR /Employee.int_DAYS_OF_THE_YEAR))
        return vacation_bonus

    # calculate todos los valuees
    severance_pay = calculate_severance_pay_interest(Employee)
    severance_pay_interest = severance_pay_interest(Employee, severance_pay)
    service_bonus = calculate_service_bonus(Employee)
    vacation = vacation(Employee)
    vacation_bonus = calculate_vacation_bonus(Employee)

    # Imprimir resultados
    print(f"Cesantías: {severance_pay}")
    print(f"severance_pay_interest: {severance_pay_interest}")
    print(f"Prima de servicios: {service_bonus}")
    print(f"vacationes: {vacation}")
    print(f"Prima de vacationes: {vacation_bonus}")

    # calculate la liquidación total
    liquidacion = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus

    # Imprimir la liquidación calculada
    print(f"Liquidación calculada: {liquidacion}")

except EmployeeException as e:
    print(e)
