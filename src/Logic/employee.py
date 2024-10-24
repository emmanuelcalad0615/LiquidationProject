class Employee:
    """
    Stores employee data at the time of severance and settlement
    """

    def __init__(self, basic_monthly_salary=0, transportation_allowance=0, worked_days=0, severance_pay_for_accrued_leave_days=0):
        self.basic_monthly_salary= basic_monthly_salary 
        self.transportation_allowance = transportation_allowance 
        self.worked_days = worked_days 
        self.severance_pay_for_accrued_leave_days = severance_pay_for_accrued_leave_days 
        self.average_salary=self.basic_monthly_salary + self.transportation_allowance
        self.DAYS_OF_THE_YEAR = 360
