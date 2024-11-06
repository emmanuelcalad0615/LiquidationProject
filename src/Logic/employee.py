"""
The `Employee` class is used to store and manage employee data related to severance pay and settlement calculations. It contains essential attributes that represent an employee's salary, allowances, and other factors that are considered in the calculation of severance or compensation (indemnización).

### Attributes:
1. **basic_monthly_salary**:
   - The basic salary of the employee per month. This is the primary factor in calculating compensation and severance pay.
   
2. **transportation_allowance**:
   - The transportation allowance the employee receives, which is added to the basic salary to calculate the total average salary.
   
3. **worked_days**:
   - The number of days the employee has worked, which can be used to calculate the total amount of severance pay depending on the contract type and duration.
   
4. **severance_pay_for_accrued_leave_days**:
   - This is the severance pay for accrued leave days that the employee is entitled to upon separation from the company.
   
5. **average_salary**:
   - The total salary the employee earns per month, which is the sum of the basic monthly salary and the transportation allowance.
   
6. **DAYS_OF_THE_YEAR**:
   - A constant representing the number of days considered in a year (360 days). This is typically used for prorating calculations like severance pay.

### Methods:
- **`__init__()`**:
   - Initializes an employee's basic monthly salary, transportation allowance, worked days, severance pay for accrued leave days, and calculates the total average salary. The class also stores a constant for the number of days in a year, set to 360 for certain financial calculations.
   
This class serves as a data structure for holding key attributes about an employee, which are later used in severance or settlement calculations, especially when determining compensation based on various contract types and work durations.

"""

class Employee:
    """
    Stores employee data at the time of severance and settlement.
    This class holds key information that will be used to calculate severance pay and settlement amounts.
    """

    def __init__(self, basic_monthly_salary=0, transportation_allowance=0, worked_days=0, severance_pay_for_accrued_leave_days=0):
        """
        Initializes an employee object with the given salary, allowances, worked days, and severance pay for accrued leave days.
        
        :param basic_monthly_salary: The basic monthly salary of the employee.
        :param transportation_allowance: The transportation allowance provided to the employee.
        :param worked_days: The number of days the employee has worked.
        :param severance_pay_for_accrued_leave_days: The severance pay for accrued leave days.
        """
        self.basic_monthly_salary = basic_monthly_salary  # The basic salary per month.
        self.transportation_allowance = transportation_allowance  # The transportation allowance.
        self.worked_days = worked_days  # The number of days worked by the employee.
        self.severance_pay_for_accrued_leave_days = severance_pay_for_accrued_leave_days  # Severance for any accrued leave days.

        # Calculate the average monthly salary, including the transportation allowance.
        self.average_salary = self.basic_monthly_salary + self.transportation_allowance

        # Constant for the number of days considered in a year (360 days is often used for calculations in the financial sector).
        self.DAYS_OF_THE_YEAR = 360
