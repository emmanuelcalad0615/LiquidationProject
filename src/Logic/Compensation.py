from datetime import datetime
import sys
sys.path.append("src")
from Logic.employee import Employee
from Logic.Liquidation import (
    EmployeeException,
    NegativeValueError,
    IncorrectDataTypeError,
    DivisionByZeroError,
    NumberOutOfRangeError
)

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
        # Verificar entradas
        verify_compensation_entries(type_of_contract, start_date, end_date)

        # Validar fechas
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        difference = end_date - start_date
        worked_days = difference.days
        worked_years = worked_days // employee.DAYS_OF_THE_YEAR
        worked_months = (worked_days % employee.DAYS_OF_THE_YEAR) // employee.DAYS_PER_MONTH

        # Contrato a término fijo de 1 año
        if type_of_contract == 'fijo_1_año':
            remaining_months = employee.MONTHS_OF_THE_YEAR - worked_months
            compensation = employee.basic_monthly_salary * remaining_months

        # Contrato a término fijo inferior a 1 año
        elif type_of_contract == 'fijo_inferior_1_año':
            remaining_months = employee.MONTHS_OF_THE_YEAR - worked_months
            compensation = max(employee.basic_monthly_salary * (remaining_months / employee.MONTHS_OF_THE_YEAR) * employee.DAYS_PER_MONTH,
                               employee.basic_monthly_salary * (MINIMUM_COMPENSATION_DAYS / employee.DAYS_PER_MONTH))

        # Contrato a término indefinido
        elif type_of_contract == 'indefinido':
            basic_monthly_salary = employee.basic_monthly_salary

            # Si el salario es menor a 13 millones (10 salarios mínimos)
            if basic_monthly_salary < 13000000:
                if worked_years <= 1:
                    # Indemnización por 1 año o menos
                    compensation = (basic_monthly_salary / 30) * 30
                else:
                    # Indemnización por el primer año
                    compensation = (basic_monthly_salary / 30) * 30
                    # Indemnización por los años adicionales
                    for year in range(2, worked_years + 1):
                        compensation += (basic_monthly_salary / 30) * 20

            # Si el salario es mayor o igual a 13 millones (más de 10 salarios mínimos)
            else:
                if worked_years <= 1:
                    # Indemnización por 1 año o menos
                    compensation = (basic_monthly_salary / 30) * 20
                else:
                    # Indemnización por el primer año
                    compensation = (basic_monthly_salary / 30) * 20
                    # Indemnización por los años adicionales
                    for year in range(2, worked_years + 1):
                        compensation += (basic_monthly_salary / 30) * 15

        return compensation

    except Exception as e:
        print(f"Error en el cálculo de la indemnización: {str(e)}")
        return None


# Crear una instancia del empleado con los parámetros necesarios
employee = Employee(
    basic_monthly_salary=2000,
    transportation_allowance=150,
    worked_days=730,  
    severance_pay_for_accrued_leave_days=365  
)
