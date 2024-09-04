# Este archivo contiene la lógica de los cálculos de la indemnización 

from datetime import datetime
import sys
sys.path.append("Logic")
from employee import Employee
from Liquidation import (
    EmployeeException,
    NegativeValue,
    IncorrectDataType,
    DivisionByZero,
    NumberOutOfRange
)

int_MINIMUM_COMPENSATION_DAYS = 15
int_DAYS_OF_SALARY_PER_YEAR = 20

def verify_compensation_entries(type_of_contract: str, start_date: str, end_date: str) -> float:
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
        # Verify entries
        verify_compensation_entries(type_of_contract, start_date, end_date)

        # Validar fechas
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Resto del cálculo...
        difference= end_date - start_date
        worked_days = difference.days

        worked_years = worked_days // employee.int_DAYS_OF_THE_YEAR
        meses_trabajados = (worked_days % employee.int_DAYS_OF_THE_YEAR) // employee.int_DAYS_PER_MONTH

        if type_of_contract == 'fijo_1_anio':
            meses_restantes = employee.meses_del_año - meses_trabajados
            indemnizacion = employee.salario_basico * meses_restantes

        elif type_of_contract == 'fijo_inferior_1_anio':
            meses_restantes = employee.meses_del_año - meses_trabajados
            indemnizacion = max(employee.salario_basico * (meses_restantes / employee.meses_del_año) * employee.int_DAYS_PER_MONTH,
                                employee.salario_basico * (MINIMO_INDEMNIZACION_DIAS / employee.int_DAYS_PER_MONTH))

        elif type_of_contract == 'indeterminado':
            if worked_years <= 1:
                indemnizacion = employee.salario_basico * employee.int_DAYS_PER_MONTH
            else:
                indemnizacion = (employee.salario_basico * employee.int_DAYS_PER_MONTH) + (employee.salario_basico * DIAS_DE_SALARIO_POR_AÑO * (worked_years - 1))

        return indemnizacion

    except Exception as e:
        print(f"Error en el cálculo de la indemnización: {str(e)}")
        return None

# Crear una instancia de employee con todos los parámetros
employee = Employee(
    basic_salary=2000,
    one_twelfth_vacation_bonus=125,
    transportation_allowance=150,
    worked_days=730,  # 2 años
    severance_pay_for_accrued_leave_days=365  # 1 año
)

# Probar cálculo de indemnización
try:
    compensation = verify_compensation_entries(employee, type_of_contract='indefinido', start_date='2020-01-01', end_date='2022-01-01')
    print(f'Indemnización calculada: {compensation}')
except Exception as e:
    print(f"Error: {str(e)}")
