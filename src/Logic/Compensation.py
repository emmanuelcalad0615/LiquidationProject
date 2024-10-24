from datetime import datetime
import sys
sys.path.append("src")
from Logic.employee import Employee
from Logic.Liquidation import (
    EmployeeException,
    NegativeValueError,
    IncorrectDataTypeError,
    DivisionByZeroError,
    NumberOutOfRangeError,    
    PERCENTAGE_OF_SEVERANCE_PAY,  # Importing the constants
    MONTHS_OF_THE_YEAR,
    DAYS_OF_THE_YEAR,
    DAYS_PER_MONTH
)

# Defining the constants for worked days 
DAYS_WORKED_FOR_GENERAL_CONTRACT = 30  
DAYS_WORKED_PER_MONTH = 30
DAYS_WORKED_FOR_SALARY_CONTRACT_AFTER_A_YEAR = 20  
DAYS_WORKED_FOR_HIGH_SALARY_CONTRACT = 15  
MINIMUM_COMPENSATION_DAYS = 15
DAYS_OF_SALARY_PER_YEAR = 20

def verify_compensation_entries(type_of_contract: str, start_date: str, end_date: str):
    if not isinstance(type_of_contract, str):
        raise IncorrectDataType('type_of_contract', str, type(type_of_contract))

    if type_of_contract not in ['fijo_1_año', 'fijo_inferior_1_año', 'indefinido']:
        raise ValueError("Tipo de contrato inválido")

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Las fechas deben estar en el formato YYYY-MM-DD")

    if start_date > end_date:
        raise ValueError("La fecha de entrada no puede ser posterior a la fecha de salida")

def calculate_compensation(employee: Employee, type_of_contract: str, start_date: str, end_date: str) -> float:
    try:
        # Verifying entries
        verify_compensation_entries(type_of_contract, start_date, end_date)

        # Validating dates
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        difference = end_date - start_date
        worked_days = difference.days
        worked_years = worked_days // DAYS_OF_THE_YEAR
        worked_months = (worked_days % DAYS_OF_THE_YEAR) // DAYS_PER_MONTH

        # 1-year fixed-term contract
        if type_of_contract == 'fijo_1_año':
            remaining_months = MONTHS_OF_THE_YEAR - worked_months
            compensation = employee.basic_monthly_salary * remaining_months

        # Fixed-term contract of less than 1 year
        elif type_of_contract == 'fijo_inferior_1_año':
            remaining_days = (MONTHS_OF_THE_YEAR - worked_months) * DAYS_PER_MONTH
            compensation = (employee.basic_monthly_salary * remaining_days) / DAYS_PER_MONTH

        # Indefinite-term contract
        elif type_of_contract == 'indefinido':
            basic_monthly_salary = employee.basic_monthly_salary

            # If the salary is less than 13 million (10 minimum wages)
            if basic_monthly_salary < 13000000:
                if worked_years <= 1:
                    # Compensation for 1 year or less
                    compensation = (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_WORKED_FOR_GENERAL_CONTRACT
                else:
                    # Compensation for the first year
                    compensation = (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_WORKED_FOR_GENERAL_CONTRACT
                    # Compensation for the additional years
                    for year in range(2, worked_years + 1):
                        compensation += (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_WORKED_FOR_SALARY_CONTRACT_AFTER_A_YEAR

            # If the salary is greater than or equal to 13 million (more than 10 minimum wages)
            else:
                if worked_years <= 1:
                    # Compensation for 1 year or less
                    compensation = (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_OF_SALARY_PER_YEAR
                else:
                    # Compensation for the first year
                    compensation = (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_OF_SALARY_PER_YEAR
                    # Compensation for the additional years
                    for year in range(2, worked_years + 1):
                        compensation += (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_WORKED_FOR_HIGH_SALARY_CONTRACT

        # Round the compensation to 2 decimal places
        return round(compensation)

    except Exception as e:
        print(f"Error en el cálculo de la indemnización: {str(e)}")
        return None
