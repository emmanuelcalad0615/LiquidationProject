#This file contains the user interface
import os
import sys

# Añadir el directorio padre al PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Logic.employee import Employee
from Logic.Liquidation import (
    calculate_severance_pay_amount,
    calculate_severance_pay_interest,
    calculate_service_bonus,
    calcute_vacation,
    calculate_vacation_bonus,
    verify_exceptions,  # Importamos la nueva función
    EmployeeException,
    NegativeValue,
    IncorrectDataType,
    DivisionByZero,
    NumberOutOfRange
)

def obtain_employee_data():
    while True:
        try:
            basic_salary = float(input("Ingrese el salario básico del empleado: "))
            one_twelfth_vacation_bonus = float(input("Ingrese un doceavo de prima de bacaciones del empleado: "))
            transportation_allowance = float(input("Ingrese el auxilio de transporte del empleado: "))
            worked_days = int(input("Ingrese los días trabajados por el empleado: "))
            severance_pay_for_accrued_leave_days = int(input("Ingrese los días liquidados para prima del empleado: "))

            employee = employee(
                basic_salary=basic_salary,
                one_twelfth_vacation_bonus=one_twelfth_vacation_bonus,
                transportation_allowance=transportation_allowance,
                worked_days=worked_days,
                severance_pay_for_accrued_leave_days=severance_pay_for_accrued_leave_days,
            )

            # Verificar excepction before proceeding
            verify_exceptions(employee)

            return employee

        except (NegativeValue, IncorrectDataType, DivisionByZero, NumberOutOfRange) as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error al crear el objeto empleado: {str(e)}")

        print("Por favor, intente nuevamente con valores válidos.")

def calculate_liquidation(employee):
    try:
        # Ya no necesitamos llamar a verify_exceptions aquí porque ya se verifica en obtain employee data
        severance_pay = calculate_severance_pay_amount(employee)
        severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
        service_bonus = calculate_service_bonus(employee)
        vacation = calcute_vacation(employee)
        vacation_bonus = calculate_vacation_bonus(employee)

        Total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus

        print("\nResultados de la liquidación:")
        print(f"Cesantías: {severance_pay}")
        print(f"calculate_severance_pay_severance_pay_interestt: {severance_pay_interest}")
        print(f"Prima de servicios: {service_bonus}")
        print(f"calcute_vacation: {vacation}")
        print(f"Prima de calcute_vacation: {vacation_bonus}")
        print(f"\nLiquidación total: {Total_liquidation}")

    except EmployeeException as e:
        print(f"\nError al calcular la liquidación: {str(e)}")

def main():
    print("Bienvenido al programa de liquidación y cálculo de indemnizaciones.")

    employee = obtain_employee_data()

    calculate_liquidation(employee)

    must_be_compensated = input("\n¿El employee debe ser indemnizado? (S/N): ").upper() == "S"

    if must_be_compensated:
        pass

if __name__ == "__main__":
    main()