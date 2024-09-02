# Este archivo contiene la lógica de los cálculos de la indemnización 

from datetime import datetime
import sys
sys.path.append("Logic")
from employee import Employee

int_MINIMUM_COMPENSATION_DAYS = 15
int_DAYS_OF_SALARY_PER_YEAR = 20

def calculate_compensation_for_dismissal(employee: Employee, type_of_contract: str, start_date: str, end_date: str) -> float:
    """
    Calcula la indemnización según el tipo de contrato y el tiempo de trabajo.

    Args:
        employee (employee): Instancia de la clase employee.
        type_of_contract (str): Tipo de contrato del employee ('fijo_1_anio', 'fijo_inferior_1_anio', 'indeterminado').
        start_date (str): Fecha de entrada en formato 'YYYY-MM-DD'.
        end_date (str): Fecha de salida en formato 'YYYY-MM-DD'.

    Returns:
        float: Monto de la indemnización.

    Raises:
        ValueError: Si el tipo de contrato es inválido.
        TypeError: Si los parámetros no son del tipo esperado.
        ValueError: Si las fechas no están en el formato correcto.
        ValueError: Si la fecha de entrada es posterior a la fecha de salida.
    """
    try:
        # Verificar tipo de contrato
        if type_of_contract not in ['fijo_1_anio', 'fijo_inferior_1_anio', 'indeterminado']:
            raise ValueError("Tipo de contrato inválido")

        # Validar fechas
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')

            if start_date > end_date:
                raise ValueError("La fecha de entrada no puede ser posterior a la fecha de salida")
        except ValueError:
            raise ValueError("Las fechas deben estar en el formato YYYY-MM-DD")

        # Resto del cálculo...
        delta = end_date - start_date
        worked_days = delta.days

        worked_years = worked_days // employee.int_DAYS_OF_THE_YEAR
        meses_trabajados = (worked_days % employee.int_DAYS_OF_THE_YEAR) // employee.int_DAYS_PER_MONTH

        if type_of_contract == 'fijo_1_anio':
            meses_restantes = employee.meses_del_año - meses_trabajados
            indemnizacion = employee.salario_basico * meses_restantes

        elif type_of_contract == 'fijo_inferior_1_anio':
            meses_restantes = employee.meses_del_año - meses_trabajados
            indemnizacion = max(employee.salario_basico * (meses_restantes / employee.meses_del_año) * employee.dias_por_mes,
                                employee.salario_basico * (MINIMUM_COMPENSATION_DAYS / employee.dias_por_mes))

        elif type_of_contract == 'indeterminado':
            if worked_years <= 1:
                indemnizacion = employee.salario_basico * employee.dias_por_mes
            else:
                indemnizacion = (employee.salario_basico * employee.dias_por_mes) + (employee.salario_basico * days of salary per year * (worked_years - 1))

        return indemnizacion

    except Exception as e:
        print(f"Error en el cálculo de la indemnización: {str(e)}")
        return None

# Crear una instancia de employee con todos los parámetros
employee = employee(
    salario_basico=2000,
    un_doceavo_prima_de_vacaciones=125,
    auxilio_de_transporte=150,
    worked_days=730,  # 2 años
    dias_liquidados_prima=365  # 1 año
)

# Probar cálculo de indemnización
try:
    indemnizacion = calcular_indemnizacion(employee, type_of_contract='indeterminado', start_date='2020-01-01', end_date='2015-01-01')
    print(f'Indemnización calculada: {indemnizacion}')
except Exception as e:
    print(f"Error: {str(e)}")
