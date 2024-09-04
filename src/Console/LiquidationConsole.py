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

def obtener_datos_employee():
    while True:
        try:
            basic_salary = float(input("Ingrese el salario básico del empleado: "))
            one_twelfth_vacation_bonus = float(input("Ingrese un doceavo de prima de bacaciones del empleado: "))
            transportation_allowance = float(input("Ingrese el auxilio de transporte del empleado: "))
            worked_days = int(input("Ingrese los días trabajados por el empleado: "))
            dias_liquidados_prima = int(input("Ingrese los días liquidados para prima del empleado: "))

            employee = employee(
                basic_salary=basic_salary,
                one_twelfth_vacation_bonus=one_twelfth_vacation_bonus,
                transportation_allowance=transportation_allowance,
                worked_days=worked_days,
                dias_liquidados_prima=dias_liquidados_prima,
            )

            # Verificar excepciones antes de proceder
            verify_exceptions(employee)

            return employee

        except (NegativeValue, IncorrectDataType, DivisionByZero, NumberOutOfRange) as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error al crear el objeto employee: {str(e)}")

        print("Por favor, intente nuevamente con valores válidos.")

def calcular_Liquidation(employee):
    try:
        # Ya no necesitamos llamar a verify_exceptions aquí porque ya se verifica en obtener_datos_employee
        cesantia = calculate_severance_pay_amount(employee)
        interes = calculate_severance_pay_interest(employee, cesantia)
        prima_servicio = calculate_service_bonus(employee)
        vacacion = calcute_vacation(employee)
        prima_vacacion = prima_de_calcute_vacation(employee)

        Liquidation_total = cesantia + interes + prima_servicio + vacacion + prima_vacacion

        print("\nResultados de la liquidación:")
        print(f"Cesantías: {cesantia}")
        print(f"calculate_severance_pay_interest: {interes}")
        print(f"Prima de servicios: {prima_servicio}")
        print(f"calcute_vacation: {vacacion}")
        print(f"Prima de calcute_vacation: {prima_vacacion}")
        print(f"\nLiquidación total: {Liquidation_total}")

    except employeeException as e:
        print(f"\nError al calcular la liquidación: {str(e)}")

def main():
    print("Bienvenido al programa de liquidación y cálculo de indemnizaciones.")

    employee = obtener_datos_employee()

    calcular_Liquidation(employee)

    debe_ser_indemnizado = input("\n¿El employee debe ser indemnizado? (S/N): ").upper() == "S"

    if debe_ser_indemnizado:
        # Aquí iría la lógica para calcular la indemnización si fuera necesario
        pass

if __name__ == "__main__":
    main()