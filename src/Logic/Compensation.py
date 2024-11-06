"""
This script contains a set of functions to calculate the compensation (severance pay) for employees based on the type of contract, the period of employment, and other factors like salary.

### Constants:
1. **PERCENTAGE_OF_SEVERANCE_PAY**: A constant that indicates the percentage used for severance calculations.
2. **MONTHS_OF_THE_YEAR**: Represents the total number of months in a year.
3. **DAYS_OF_THE_YEAR**: The total number of days in a year, typically 365.
4. **DAYS_PER_MONTH**: The average number of days in a month, typically 30.
5. **DAYS_WORKED_FOR_GENERAL_CONTRACT**: Number of days worked used for general contracts in severance calculations.
6. **DAYS_WORKED_PER_MONTH**: Number of days worked per month used in severance calculations.
7. **DAYS_WORKED_FOR_SALARY_CONTRACT_AFTER_A_YEAR**: Days worked used for salary-based contracts after a year.
8. **DAYS_WORKED_FOR_HIGH_SALARY_CONTRACT**: The number of days used for contracts with high salaries.
9. **MINIMUM_COMPENSATION_DAYS**: The minimum number of days that an employee can be compensated for, typically a minimum threshold for severance pay.
10. **DAYS_OF_SALARY_PER_YEAR**: A predefined constant representing the days of salary entitlement per year.

### Functions:

1. **verify_compensation_entries(type_of_contract, start_date, end_date)**:
   - Verifies the contract type and date formats.
   - Ensures the contract type is valid (either 'fijo_1_año', 'fijo_inferior_1_año', or 'indefinido').
   - Validates the start and end dates by ensuring they follow the correct format (`YYYY-MM-DD`).
   - Ensures that the start date is not later than the end date.
   
2. **calculate_compensation(employee, type_of_contract, start_date, end_date)**:
   - This is the main function for calculating the severance pay (indemnización).
   - It validates the contract type, start and end dates using `verify_compensation_entries`.
   - It calculates the total number of worked days, months, and years between the start and end dates.
   - Depending on the contract type, it applies different logic to compute the severance pay:
     - **'fijo_1_año'**: Compensation is based on the remaining months of the first year.
     - **'fijo_inferior_1_año'**: Compensation is calculated for the remaining days in the current year.
     - **'indefinido'**: Compensation is calculated differently depending on the salary, with different rates for low salary employees (less than 13 million) and high salary employees (greater than or equal to 13 million).
   - The compensation is rounded to two decimal places before being returned.

3. **Error Handling**:
   - The function handles several exceptions such as:
     - Incorrect data types (e.g., if the `type_of_contract` is not a string).
     - Invalid contract types or dates.
     - General errors during compensation calculation.

### Example:

- For an indefinite contract (`'indefinido'`), the function calculates severance pay based on the employee's salary and the years worked:
  - For employees earning less than 13 million, compensation is calculated based on a general rate (for the first year) and additional years worked.
  - For employees earning more than 13 million, the compensation rate changes after the first year of work, with higher compensation rates for the following years.

### Exceptions:
1. **EmployeeException**: General exception for any employee-related errors.
2. **NegativeValueError**: Raised when there is a negative value input (e.g., negative salary).
3. **IncorrectDataTypeError**: Raised when there is an incorrect data type, such as passing a non-string value for `type_of_contract`.
4. **DivisionByZeroError**: Raised when an operation attempts to divide by zero (e.g., in salary calculations).
5. **NumberOutOfRangeError**: Raised when any of the numbers involved (such as salary or days) fall outside of the expected range.

The main goal of this script is to calculate and validate severance compensation based on the type of contract and employment duration, with various rules applied to different types of contracts and salary levels.

"""

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

# Constants for worked days in different scenarios
DAYS_WORKED_FOR_GENERAL_CONTRACT = 30  
DAYS_WORKED_PER_MONTH = 30
DAYS_WORKED_FOR_SALARY_CONTRACT_AFTER_A_YEAR = 20  
DAYS_WORKED_FOR_HIGH_SALARY_CONTRACT = 15  
MINIMUM_COMPENSATION_DAYS = 15
DAYS_OF_SALARY_PER_YEAR = 20

def verify_compensation_entries(type_of_contract: str, start_date: str, end_date: str):
    """
    Verifies the contract type, start date, and end date inputs.
    Ensures correct format and logical consistency.
    """
    if not isinstance(type_of_contract, str):
        raise IncorrectDataTypeError('type_of_contract', str, type(type_of_contract))

    if type_of_contract not in ['fijo_1_año', 'fijo_inferior_1_año', 'indefinido']:
        raise ValueError("Invalid contract type.")

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Dates must be in the format YYYY-MM-DD.")

    if start_date > end_date:
        raise ValueError("The start date cannot be later than the end date.")

def calculate_compensation(employee: Employee, type_of_contract: str, start_date: str, end_date: str) -> float:
    """
    Calculates the compensation (severance pay) based on the type of contract, 
    start and end dates, and the employee's salary.
    """
    try:
        # Verify the inputs first
        verify_compensation_entries(type_of_contract, start_date, end_date)

        # Convert date strings into datetime objects
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # Calculate the difference in days and convert into years and months
        difference = end_date - start_date
        worked_days = difference.days
        worked_years = worked_days // DAYS_OF_THE_YEAR
        worked_months = (worked_days % DAYS_OF_THE_YEAR) // DAYS_PER_MONTH

        # Compensation calculation logic for each contract type
        if type_of_contract == 'fijo_1_año':
            remaining_months = MONTHS_OF_THE_YEAR - worked_months
            compensation = employee.basic_monthly_salary * remaining_months

        elif type_of_contract == 'fijo_inferior_1_año':
            remaining_days = (MONTHS_OF_THE_YEAR - worked_months) * DAYS_PER_MONTH
            compensation = (employee.basic_monthly_salary * remaining_days) / DAYS_PER_MONTH

        elif type_of_contract == 'indefinido':
            basic_monthly_salary = employee.basic_monthly_salary

            if basic_monthly_salary < 13000000:
                if worked_years <= 1:
                    compensation = (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_WORKED_FOR_GENERAL_CONTRACT
                else:
                    compensation = (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_WORKED_FOR_GENERAL_CONTRACT
                    for year in range(2, worked_years + 1):
                        compensation += (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_WORKED_FOR_SALARY_CONTRACT_AFTER_A_YEAR
            else:
                if worked_years <= 1:
                    compensation = (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_OF_SALARY_PER_YEAR
                else:
                    compensation = (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_OF_SALARY_PER_YEAR
                    for year in range(2, worked_years + 1):
                        compensation += (basic_monthly_salary / DAYS_PER_MONTH) * DAYS_WORKED_FOR_HIGH_SALARY_CONTRACT

        # Round the compensation to 2 decimal places
        return round(compensation)

    except Exception as e:
        print(f"Error calculating compensation: {str(e)}")
        return None
