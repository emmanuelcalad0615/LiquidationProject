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
    calculate_vacation_bonus,
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
        """Configura el estado inicial para cada prueba"""
        self.start_date = datetime(2019, 10, 28)
        self.end_date = datetime(2020, 8, 8)

    def testLiquidation1(self):
        employee = Employee(
            basic_salary=5689500,
            one_twelfth_vacation_bonus=5741427,
            transportation_allowance=0,
            worked_days=729,
            severance_pay_for_accrued_leave_days=310,
        )
        expected_value=50137036
        try:
            verify_exceptions(employee)
            severance_pay = calculate_severance_pay_amount(employee)
            severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
            service_bonus = calculate_service_bonus(employee)
            vacation = calculate_vacation(employee)
            vacation_bonus = calculate_vacation_bonus(employee)

            total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
            self.assertEqual(total_liquidation, expected_value)

        except EmployeeException as e:
            self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation2(self):
            employee = Employee(
                basic_salary=900803,
                one_twelfth_vacation_bonus=0,
                transportation_allowance=80500,
                worked_days=80,
                severance_pay_for_accrued_leave_days=59,
            )
            expected_value=584885
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)
                vacation_bonus = calculate_vacation_bonus(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")
    def testLiquidation3(self):
            employee = Employee(
                basic_salary=1450023,
                one_twelfth_vacation_bonus=0,
                transportation_allowance=120018,
                worked_days=169,
                severance_pay_for_accrued_leave_days=30,
            )
            expected_value=1590110
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)
                vacation_bonus = calculate_vacation_bonus(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation4(self):
            employee = Employee(
                basic_salary=3638092,
                one_twelfth_vacation_bonus=0,
                transportation_allowance=0,
                worked_days=888,
                severance_pay_for_accrued_leave_days=154,
            )
            expected_value=22160507
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)
                vacation_bonus = calculate_vacation_bonus(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:

                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation5(self):
        employee = Employee(
            basic_salary=5128350,
            one_twelfth_vacation_bonus=854725,
            transportation_allowance=500854,
            worked_days=120,
            severance_pay_for_accrued_leave_days=79,
        )
        expected_value = 5380074
        try:
            verify_exceptions(employee)
            severance_pay = calculate_severance_pay_amount(employee)
            severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
            service_bonus = calculate_service_bonus(employee)
            vacation = calculate_vacation(employee)
            vacation_bonus = calculate_vacation_bonus(employee)

            total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
            self.assertEqual(total_liquidation, expected_value)

        except EmployeeException as e:
            self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation6(self):
        employee = Employee(
            basic_salary=877803,
            one_twelfth_vacation_bonus=0,
            transportation_allowance=102854,
            worked_days=210,
            severance_pay_for_accrued_leave_days=169,
        )
        expected_value=1584510
        try:
            verify_exceptions(employee)
            severance_pay = calculate_severance_pay_amount(employee)
            severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
            service_bonus = calculate_service_bonus(employee)
            vacation = calculate_vacation(employee)
            vacation_bonus = calculate_vacation_bonus(employee)

            total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
            self.assertEqual(total_liquidation, expected_value)

        except EmployeeException as e:

            self.fail(f"Error al calcular la liquidación: {str(e)}")
    # Casos extraordinarios

    def testLiquidation7(self):
            employee = Employee(
                basic_salary=5689500,
                one_twelfth_vacation_bonus=0,
                transportation_allowance=0,
                worked_days=999,
                severance_pay_for_accrued_leave_days=999,
            )
            expected_value=52622611
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)
                vacation_bonus = calculate_vacation_bonus(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")


    def testLiquidation8(self):
            employee = Employee(
                basic_salary=900803,
                one_twelfth_vacation_bonus=0,
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
                vacation_bonus = calculate_vacation_bonus(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:

                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation9(self):
            employee = Employee(
                basic_salary=3450023,
                one_twelfth_vacation_bonus=0,
                transportation_allowance=0,
                worked_days=69,
                severance_pay_for_accrued_leave_days=0,
            )
            expected_value=1337717
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)
                vacation_bonus = calculate_vacation_bonus(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation10(self):
            employee = Employee(
                basic_salary=26660000,
                one_twelfth_vacation_bonus=0,
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
                vacation_bonus = calculate_vacation_bonus(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:

                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation11(self):
            employee = Employee(
                basic_salary=2230000,
                one_twelfth_vacation_bonus=0,
                transportation_allowance=0,
                worked_days=1,
                severance_pay_for_accrued_leave_days=400,
            )
            expected_value=2490168
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)
                vacation_bonus = calculate_vacation_bonus(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:

                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation12(self):
            employee = Employee(
                basic_salary=4300000,
                one_twelfth_vacation_bonus=0,
                transportation_allowance=0,
                worked_days=1,
                severance_pay_for_accrued_leave_days=1,
            )
            expected_value=35836
            try:
                verify_exceptions(employee)
                severance_pay = calculate_severance_pay_amount(employee)
                severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
                service_bonus = calculate_service_bonus(employee)
                vacation = calculate_vacation(employee)
                vacation_bonus = calculate_vacation_bonus(employee)

                total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation + vacation_bonus
                self.assertEqual(total_liquidation, expected_value)

            except EmployeeException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")

    # Casos de error
    def testLiquidation13(self):
        """ Basic salary negative"""
        employee = Employee(
            basic_salary=-12895,
            one_twelfth_vacation_bonus=0,
            transportation_allowance=5654889,
            worked_days=8,
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NegativeValueError):
            verify_exceptions(employee)



    def testLiquidation14(self):
        """Negative salary for worked days"""
        employee = Employee(
            basic_salary=-1000000,  
            one_twelfth_vacation_bonus=50000,
            transportation_allowance=20000,
            worked_days=-30,
            severance_pay_for_accrued_leave_days=10,
        )
        with self.assertRaises(NegativeValueError):
            verify_exceptions(employee)

    def testLiquidation15(self):
        """ Negative worked days """
        employee = Employee(
            basic_salary=-12895,
            one_twelfth_vacation_bonus=0,
            transportation_allowance=5654889,
            worked_days=8,
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NegativeValueError):
            verify_exceptions(employee)

    def testLiquidation16(self):
        """ Negative basic salary """
        employee = Employee(
            basic_salary=-1000000,  # Valor negativo
            one_twelfth_vacation_bonus=50000,
            transportation_allowance=20000,
            worked_days=30,
            severance_pay_for_accrued_leave_days=10,
        )
        with self.assertRaises(NegativeValueError):
            verify_exceptions(employee)

    def testLiquidation17(self):
        """ Incorrect data """
        employee = Employee(
            basic_salary="sapo",
            one_twelfth_vacation_bonus=0,
            transportation_allowance=5654889,
            worked_days=8,
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NonNumericValueError):
            verify_exceptions(employee)

    def testLiquidation18(self):
        """ Incorrect Data """
        employee = Employee(
            basic_salary=194985,
            one_twelfth_vacation_bonus=0,
            transportation_allowance=5654889,
            worked_days=8,
            severance_pay_for_accrued_leave_days="no me dijieron en la empresa",
        )
        with self.assertRaises(NonNumericValueError):
            verify_exceptions(employee)

    def testLiquidation19(self):
        """ Incorrect Data """
        employee = Employee(
            basic_salary=18999,
            one_twelfth_vacation_bonus="soy pobre",
            transportation_allowance=5654889,
            worked_days=8,
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NonNumericValueError):
            verify_exceptions(employee)

    def testLiquidation20(self):
        """ Incorrect data """
        employee = Employee(
            basic_salary="sapo",
            one_twelfth_vacation_bonus=0,
            transportation_allowance="error_data",
            worked_days=8,
            severance_pay_for_accrued_leave_days=18,
        )
        with self.assertRaises(NonNumericValueError):
            verify_exceptions(employee)


if __name__ == "__main__":
    unittest.main()
