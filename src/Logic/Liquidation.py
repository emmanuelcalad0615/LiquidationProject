"""
This script defines several custom exceptions, constants, and functions related to the calculation of employee severance pay, service bonuses, and vacation days. The logic revolves around determining the total settlement amount, or "liquidation," for an employee based on various financial factors such as salary, worked days, and accrued benefits.

### Custom Exceptions:
1. **EmployeeException**: The base class for all exceptions related to employee data and calculations.
   
2. **NegativeValueError**: Raised when a field in the employee data contains a negative value.
   
3. **IncorrectDataTypeError**: Raised when the data type of a field doesn't match the expected type.
   
4. **DivisionByZeroError**: Raised when there is an attempt to divide by zero (used for validating constants).
   
5. **NumberOutOfRangeError**: Raised when a number in a field is outside an allowed range.
   
6. **NonNumericValueError**: Raised when a value is expected to be numeric but isn't.

### Functions:

#### **validate_input(field, value, expected_type)**
Validates the input values for specific fields:
- Ensures the value is of the expected type.
- Attempts to convert values to numeric types (float) if they are not the correct type.
- Checks if the value is negative.

#### **verify_exceptions(employee)**
Verifies the input values of an `Employee` object:
- Calls `validate_input()` to validate fields such as `basic_monthly_salary`, `transportation_allowance`, `worked_days`, and `severance_pay_for_accrued_leave_days`.

#### **verify_constants()**
Validates constants used in the calculations to ensure there are no divisions by zero.

#### **calculate_severance_pay_amount(employee)**
Calculates the severance pay for an employee based on their average salary and worked days:
- The formula used: 
  \[
  \text{Severance Pay} = \left( \frac{\text{Average Salary} \times \text{Worked Days}}{\text{Days of the Year}} \right)
  \]

#### **calculate_severance_pay_interest(employee, severance_pay)**
Calculates the interest on severance pay based on a percentage of the total severance pay:
- The formula used:
  \[
  \text{Severance Pay Interest} = \left( \frac{\text{Severance Pay} \times \text{Worked Days} \times \text{Severance Pay Percentage}}{\text{Days of the Year}} \right)
  \]

#### **calculate_service_bonus(employee)**
Calculates the service bonus based on the employee's average salary and worked days:
- The formula used is the same as the severance pay calculation:
  \[
  \text{Service Bonus} = \left( \frac{\text{Average Salary} \times \text{Worked Days}}{\text{Days of the Year}} \right)
  \]

#### **calculate_vacation(employee)**
Calculates vacation days based on the employee's basic monthly salary and worked days:
- The formula used:
  \[
  \text{Vacation} = \left( \frac{\text{Basic Monthly Salary} \times \text{Worked Days}}{\text{Hours Worked in a Semester}} \right)
  \]

#### **calculate_liquidation(employee)**
The main function that calculates the full settlement amount for an employee:
- Calls the verification functions (`verify_exceptions` and `verify_constants`).
- Uses helper functions (`calculate_severance_pay_amount`, `calculate_severance_pay_interest`, `calculate_service_bonus`, `calculate_vacation`) to compute the severance pay, interest, service bonus, vacation, and total settlement.
- Returns a dictionary with the detailed breakdown of the total liquidation.

### Constants:
1. **PERCENTAGE_OF_SEVERANCE_PAY**: The percentage rate used to calculate the severance pay interest.
2. **MONTHS_OF_THE_YEAR**: The number of months in a year (12).
3. **DAYS_OF_THE_YEAR**: The number of days in a year (360) used for prorating.
4. **VACATION_PER_YEAR**: The number of vacation days an employee is entitled to per year.
5. **DAYS_PER_MONTH**: The number of days in a month (30).
6. **HALF_A_SEMESTER_WORKED**: Used for calculating semestral premium installments.
7. **DAYS_WORKED_IN_THE_SEMESTER**: The number of days worked in a semester (180).
8. **TOTAL_SEMIANNUAL_PREMIUM_INSTALLMENTS**: The fraction of the premium paid biannually.
9. **HOUR_WORKED_IN_A_SEMESTER**: The number of hours worked in a semester (720).

The functions and constants in this module are used for calculating the final liquidation, which includes severance pay, interest on severance, service bonuses, and vacation days, based on an employee's salary and tenure.
"""

import sys
sys.path.append("src")

from Logic.employee import Employee
from decimal import Decimal, ROUND_HALF_UP

# Definition of custom exceptions
class EmployeeException(Exception):
    """Base class for exceptions related to the Employee class."""
    pass

class NegativeValueError(EmployeeException):
    """Exception for negative values."""
    def __init__(self, field, value):
        self.field = field
        self.value = value
        super().__init__(f"Error: The value '{value}' in the field '{field}' cannot be negative.")

class IncorrectDataTypeError(EmployeeException):
    """Exception for incorrect data types."""
    def __init__(self, field, expected_type, actual_type):
        self.field = field
        self.expected_type = expected_type
        self.actual_type = actual_type
        super().__init__(f"Error: The data type of the field '{field}' should be '{expected_type.__name__}' but received '{actual_type.__name__}'.")

class DivisionByZeroError(EmployeeException):
    """Exception for division by zero."""
    def __init__(self, message="Error: Division by zero detected."):
        super().__init__(message)

class NumberOutOfRangeError(EmployeeException):
    """Exception for numbers out of range."""
    def __init__(self, field, allowed_range, value):
        self.field = field
        self.allowed_range = allowed_range
        self.value = value
        super().__init__(f"Error: The value '{value}' in the field '{field}' is outside the allowed range {allowed_range}.")

class NonNumericValueError(EmployeeException):
    """Exception for non-numeric values."""
    def __init__(self, field, value):
        self.field = field
        self.value = value
        super().__init__(f"Error: The value '{value}' in the field '{field}' is not a valid number.")


def validate_input(field, value, expected_type):
    """
    Validates the value of a field, ensuring that its type is correct
    and that the value is not negative.

    Args:
    - field (str): The name of the field being validated.
    - value (any): The value of the field being validated.
    - expected_type (type): The expected data type for the field.

    Raises:
    - IncorrectDataTypeError: If the value does not have the expected type.
    - NonNumericValueError: If the value cannot be converted to a number.
    - NegativeValueError: If the value is negative.
    """
    # Check if the value is of the expected type
    if not isinstance(value, expected_type):
        try:
            # Try converting the value to float to check if it's numeric
            float(value)
        except (ValueError, TypeError):
            # If the conversion fails, it's a non-numeric value
            raise NonNumericValueError(field, value)
        # If the conversion succeeds but the type is incorrect, raise an IncorrectDataTypeError
        raise IncorrectDataTypeError(field, expected_type, type(value))

    # Check if the value is negative
    if value < 0:
        raise NegativeValueError(field, value)


def verify_exceptions(employee):
    """
    Verifies that the fields of the `employee` object do not contain data type errors or negative values.

    Args:
    - employee (Employee): Employee object containing the data to be validated.

    Raises:
    - NegativeValueError: If any field contains a negative value.
    - IncorrectDataTypeError: If any field has an incorrect data type.
    """
    # Check the data types and negative values for important fields
    validate_input("basic_monthly_salary", employee.basic_monthly_salary, (int, float))
    validate_input("transportation_allowance", employee.transportation_allowance, (int, float))
    validate_input("worked_days", employee.worked_days, int)
    validate_input("severance_pay_for_accrued_leave_days", employee.severance_pay_for_accrued_leave_days, int)


def verify_constants():
    """
    Verifies the constants used in calculations to ensure there are no errors,
    such as division by zero.

    Raises:
    - DivisionByZeroError: If any constant used in divisions is zero.
    """
    # Validate that the constants are not zero, as they are used in divisions
    if DAYS_OF_THE_YEAR == 0:
        raise DivisionByZeroError("Error: 'DAYS_OF_THE_YEAR' cannot be zero.")
    if HALF_A_SEMESTER_WORKED == 0:
        raise DivisionByZeroError("Error: 'HALF_A_SEMESTER_WORKED' cannot be zero.")
    if DAYS_PER_MONTH == 0:
        raise DivisionByZeroError("Error: 'DAYS_PER_MONTH' cannot be zero.")


# Function to calculate the severance pay amount
def calculate_severance_pay_amount(employee: Employee):
    """
    Calculates the severance pay amount based on the worked days
    and the employee's average salary.

    Args:
    - employee (Employee): Employee object containing the average salary and worked days.

    Returns:
    - float: Severance pay amount.
    """
    # Formula: (average salary * worked days) / days in the year
    severance_pay = ((employee.average_salary * employee.worked_days) / DAYS_OF_THE_YEAR)
    return severance_pay


# Function to calculate the interest amount on severance pay
def calculate_severance_pay_interest(employee: Employee, severance_pay):
    """
    Calculates the interest on the severance pay, based on the percentage
    of severance pay and the worked days.

    Args:
    - employee (Employee): Employee object with worked days.
    - severance_pay (float): Previously calculated severance pay amount.

    Returns:
    - float: Interest amount on the severance pay.
    """
    # Formula: (severance pay * worked days * severance pay percentage) / days in the year
    severance_pay_interest = ((severance_pay * employee.worked_days * PERCENTAGE_OF_SEVERANCE_PAY) / DAYS_OF_THE_YEAR)
    return severance_pay_interest


# Function to calculate the service bonus amount
def calculate_service_bonus(employee: Employee):
    """
    Calculates the service bonus based on the employee's average salary and worked days.

    Args:
    - employee (Employee): Employee object containing the average salary and worked days.

    Returns:
    - float: Service bonus amount.
    """
    # Formula: (average salary * worked days) / days in the year
    service_bonus = ((employee.average_salary * employee.worked_days) / DAYS_OF_THE_YEAR)
    return service_bonus


# Function to calculate the vacation days amount
def calculate_vacation(employee: Employee):
    """
    Calculates the vacation pay based on the employee's basic monthly salary
    and the worked days.

    Args:
    - employee (Employee): Employee object with basic salary and worked days.

    Returns:
    - float: Vacation pay amount.
    """
    # Formula: (basic monthly salary * worked days) / hours worked in a semester
    vacation = ((employee.basic_monthly_salary * employee.worked_days) / HOUR_WORKED_IN_A_SEMESTER)
    return vacation


# Function to calculate the final settlement amount
def calculate_liquidation(employee):
    """
    Calculates the total settlement amount for an employee, which includes severance pay,
    interest on severance pay, service bonus, and vacation days.

    Args:
    - employee (Employee): Employee object containing the data for the settlement calculation.

    Returns:
    - dict: A dictionary containing the breakdown of the settlement, including severance pay,
            severance pay interest, service bonus, vacation, and total settlement.
    """
    # Validate the employee object for any errors
    verify_exceptions(employee)
    
    # Validate the constants used in the calculations
    verify_constants()

    # Calculate all the components of the settlement
    severance_pay = calculate_severance_pay_amount(employee)
    severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
    service_bonus = calculate_service_bonus(employee)
    vacation = calculate_vacation(employee)
    
    # Sum all the components to get the total settlement and round the result
    total_liquidation = round(severance_pay + severance_pay_interest + service_bonus + vacation)
    
    # Return the results in a dictionary
    return {
        "severance_pay": severance_pay,
        "severance_pay_interest": severance_pay_interest,
        "service_bonus": service_bonus,
        "vacation": vacation,
        "total_liquidation": total_liquidation
    }
