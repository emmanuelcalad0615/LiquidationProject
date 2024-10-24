import os
import sys
from datetime import datetime

# This adds the parent directory to the PATH
sys.path.append("src")

# Importing the modules
from Logic.employee import Employee
from Logic.Liquidation import (
    calculate_severance_pay_amount,
    calculate_severance_pay_interest,
    calculate_service_bonus,
    calculate_vacation,
    verify_exceptions,  
    EmployeeException,
    NegativeValueError,
    IncorrectDataTypeError,
    DivisionByZeroError,
    NumberOutOfRangeError
)
from Logic.Compensation import calculate_compensation

def get_employee_data():
    while True:
        try:
            basic_monthly_salary = float(input("Ingrese su salario básico mensual: "))
            transportation_allowance = float(input("Ingrese su auxilio de transporte: "))
            worked_days = int(input("Ingrese su total de días trabajados: "))

            # Create an instance of Employee
            employee = Employee(
                basic_monthly_salary=basic_monthly_salary,
                transportation_allowance=transportation_allowance,
                worked_days=worked_days,
            )

            # Verify the exceptions antes de proceder
            verify_exceptions(employee)

            return employee

        except (NegativeValueError, IncorrectDataTypeError, DivisionByZeroError , NumberOutOfRangeError) as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error al crear el objeto empleado: {str(e)}")

        print("Por favor, intente nuevamente con valores válidos.")

def calculate_liquidation(employee):
    try:
        # Calculate different components of liquidation
        severance_pay = calculate_severance_pay_amount(employee)
        severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
        service_bonus = calculate_service_bonus(employee)
        vacation = calculate_vacation(employee)
        #vacation_bonus = calculate_vacation_bonus(employee)

        total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation #+ vacation_bonus

        print("\nResultados de la liquidación:")
        print(f"Cesantías: {severance_pay}")
        print(f"Intereses de cesantías: {severance_pay_interest}")
        print(f"Prima de servicios: {service_bonus}")
        print(f"Vacaciones: {vacation}")
        #print(f"Prima de vacaciones: {vacation_bonus}")
        print(f"\nLiquidación total: {total_liquidation}")

    except EmployeeException as e:
        print(f"\nError al calcular la liquidación: {str(e)}")

def calculate_compensation_with_indefinite_contract(employee, start_date, end_date):
    """
    Función adicional para manejar la lógica específica de los contratos indefinidos,
    donde se le pregunta al usuario si la indemnización es solo por el primer año o por más años.
    """
    first_year_only = input("¿La indemnización solo es por el primer año? (S/N): ").strip().upper()
    
    if first_year_only == 'S':
        # Calculates the first year
        compensation = calculate_compensation(employee, "indefinido", start_date, end_date)
    else:
        # Calculates more than 1 year
        compensation = calculate_compensation(employee, "indefinido", start_date, end_date)

    return compensation

def main():
    print("Bienvenido al programa de liquidación y cálculo de indemnizaciones.")

    employee = get_employee_data()

    calculate_liquidation(employee)

    must_be_compensated = input("\n¿El empleado debe ser indemnizado? (S/N): ").upper() == "S"

    if must_be_compensated:
        type_of_contract = input("Ingrese el tipo de contrato (fijo_1_año, fijo_inferior_1_año, indefinido): ").strip().lower()
        start_date = input("Ingrese la fecha de inicio del contrato (YYYY-MM-DD): ").strip()
        end_date = input("Ingrese la fecha de finalización del contrato (YYYY-MM-DD): ").strip()

        try:
            if type_of_contract == "indefinido":
                # Si el contrato es indefinido, llamar a la función específica
                compensation = calculate_compensation_with_indefinite_contract(employee, start_date, end_date)
            else:
                # Para otros tipos de contrato, calcular normalmente
                compensation = calculate_compensation(employee, type_of_contract, start_date, end_date)

            if compensation is not None:
                print(f"Indemnización calculada: {compensation}")
        except Exception as e:
            print(f"Error al calcular la indemnización: {str(e)}")

if __name__ == "__main__":
    main()
