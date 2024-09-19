class Employee:
    """
    Stores employee data at the time of severance and settlement
    """

    def __init__(self, basic_monthly_salary=0, transportation_allowance=0, worked_days=0, severance_pay_for_accrued_leave_days=0):
        self.basic_monthly_salary= basic_monthly_salary 
        self.transportation_allowance = transportation_allowance 
        self.worked_days = worked_days 
        self.severance_pay_for_accrued_leave_days = severance_pay_for_accrued_leave_days 
        self.PERCENTAGE_OF_SEVERANCE_PAY = 0.12 
        self.MONTHS_OF_THE_YEAR = 12
        self.DAYS_OF_THE_YEAR = 360 
        self.VACATION_PER_YEAR = 15 
        self.DAYS_PER_MONTH = 30
        self.HALF_A_SEMESTER_WORKED = 2 
        self.DAYS_WORKED_IN_THE_SEMESTER = 180 
        self.TOTAL_SEMIANNUAL_PREMIUM_INSTALLMENTS = 0.6 
        self.average_salary=self.basic_monthly_salary + self.transportation_allowance
        self.HOUR_WORKED_IN_A_SEMESTER = 720


    