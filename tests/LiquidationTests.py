import os
import sys
import unittest
sys.path.append("src")
from datetime import datetime
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
    NumberOutOfRangeError,
    NonNumericValueError
)

class LiquidationTest(unittest.TestCase):
    def setUp(self):
        """Set the initial state for each test"""
        self.start_date = datetime(2019, 10, 28)
        self.end_date = datetime(2020, 8, 8)

    def testLiquidation1(self):
        employee = Employee(
            basic_monthly_salary=689455,
            transportation_allowance=77700,
            worked_days=360
)
        expected_value=(1971097)
        try:
            verify_exceptions(employee)
            severance_pay = calculate_severance_pay_amount(employee)
            severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
            service_bonus = calculate_service_bonus(employee)
            vacation = calculate_vacation(employee)


            total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
            self.assertEqual(total_liquidation, expected_value)

        except EmployeeException as e:
            self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation2(self):
            employee = Employee(
                basic_monthly_salary=1000000,
                transportation_allowance=77700,
                worked_days=180

            )
            expected_value=1360031
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)


                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")
    def testLiquidation3(self):
            employee = Employee(
                basic_monthly_salary=5689500,
                transportation_allowance=0,
                worked_days=729
            )
            expected_value=31602754
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)


                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation4(self):
            employee = Employee(
                basic_monthly_salary=900803,
                transportation_allowance=80500,
                worked_days=80
            )
            expected_value= (542039)
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)


                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:

                self.fail(f"Error al calcular la liquidación: {str(e)}")
        
    def testLiquidation5(self):
        employee = Employee(
            basic_monthly_salary=1450023,
            transportation_allowance=120018,
            worked_days=169
        )
        expected_value = 1855967
        try:
            verify_exceptions(employee)
            severance_pay = calculate_severance_pay_amount(employee)
            severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
            service_bonus = calculate_service_bonus(employee)
            vacation = calculate_vacation(employee)


            total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
            self.assertEqual(total_liquidation, expected_value)

        except EmployeeException as e:
            self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation6(self):
        employee = Employee(
            basic_monthly_salary=3638092,
            transportation_allowance=0,
            worked_days=888
        )
        expected_value=25091193
        try:
            verify_exceptions(employee)
            severance_pay = calculate_severance_pay_amount(employee)
            severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
            service_bonus = calculate_service_bonus(employee)
            vacation = calculate_vacation(employee)


            total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
            self.assertEqual(total_liquidation, expected_value)

        except EmployeeException as e:

            self.fail(f"Error al calcular la liquidación: {str(e)}")
            
            # Usar assertAlmostEqual para permitir un margen de error


    # Extraordinary cases

    def testLiquidation7(self):
            employee = Employee(
                basic_monthly_salary=5689500,
                transportation_allowance=0,
                worked_days=999,
                severance_pay_for_accrued_leave_days=999,
            )
            expected_value=573117541
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)


                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")


    def testLiquidation8(self):
            employee = Employee(
                basic_monthly_salary=900803,
                transportation_allowance=80500,
                worked_days=0,
                severance_pay_for_accrued_leave_days=0,
            )
            expected_value=0
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:

                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation9(self):
            employee = Employee(
                basic_monthly_salary=3450023,
                transportation_allowance=0,
                worked_days=69,
                severance_pay_for_accrued_leave_days=0,
            )
            expected_value=2843392
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)


                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation10(self):
            employee = Employee(
                basic_monthly_salary=26660000,
                transportation_allowance=0,
                worked_days=0,
                severance_pay_for_accrued_leave_days=0,
            )
            expected_value=0
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:

                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation11(self):
            employee = Employee(
                basic_monthly_salary=2230000,
                transportation_allowance=0,
                worked_days=1,
                severance_pay_for_accrued_leave_days=400,
            )
            expected_value=2490372
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)


                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:

                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation12(self):
            employee = Employee(
                basic_monthly_salary=4300000,
                transportation_allowance=0,
                worked_days=1,
                severance_pay_for_accrued_leave_days=1,
            )
            expected_value=36230
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)


                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation 
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")

    # Error cases
    def testLiquidation13(self):
        """ Basic salary negative"""
        employee = Employee(
            basic_monthly_salary=-12895,
            transportation_allowance=5654889,
            worked_days=8,
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NegativeValueError):
            verify_exceptions(employee)



    def testLiquidation14(self):
        """Negative salary for worked days"""
        employee = Employee(
            basic_monthly_salary=-1000000,
            transportation_allowance=20000,
            worked_days=-30,
            severance_pay_for_accrued_leave_days=10,
        )
        with self.assertRaises(NegativeValueError):
            verify_exceptions(employee)

    def testLiquidation15(self):
        """ Negative worked days """
        employee = Employee(
            basic_monthly_salary=-12895,
            transportation_allowance=5654889,
            worked_days=8,
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NegativeValueError):
            verify_exceptions(employee)

    def testLiquidation16(self):
        """ Negative basic salary """
        employee = Employee(
            basic_monthly_salary=-1000000,  
            transportation_allowance=20000,
            worked_days=30,
            severance_pay_for_accrued_leave_days=10,
        )
        with self.assertRaises(NegativeValueError):
            verify_exceptions(employee)

    def testLiquidation17(self):
        """ Incorrect data """
        employee = Employee(
            basic_monthly_salary=1999,
            transportation_allowance=5654889,
            worked_days="sapo",
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NonNumericValueError):
            verify_exceptions(employee)

    def testLiquidation18(self):
        """ Incorrect Data """
        employee = Employee(
            basic_monthly_salary="no me dijieron en la empresa",
            transportation_allowance=5654889,
            worked_days=8,
            severance_pay_for_accrued_leave_days=1777777,
        )
        with self.assertRaises(NonNumericValueError):
            verify_exceptions(employee)

    def testLiquidation19(self):
        """ Incorrect Data """
        employee = Employee(
            basic_monthly_salary=18999,
            transportation_allowance=5654889,
            worked_days="hola soy un simple trabajador",
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NonNumericValueError):
            verify_exceptions(employee)

    def testLiquidation20(self):
        """ Incorrect data """
        employee = Employee(
            basic_monthly_salary=18999,
            transportation_allowance=1555555,
            worked_days="error_data",
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NonNumericValueError):
            verify_exceptions(employee)


if __name__ == "__main__":
    unittest.main()
