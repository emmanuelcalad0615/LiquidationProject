# En este archivo va la inicialización de todas las variables necesarias
class Employee:
    """
    Almacena los datos del empleado a la hora de la indemnizacion y liquidacion
    """

    def __init__(self, basic_salary=0, one_twelfth_vacation_bonus=0, transportation_allowance=0, worked_days=0, severance_pay_for_accrued_leave_days=0):
        self.basic_salary = basic_salary
        self.one_twelfth_vacation_bonus = one_twelfth_vacation_bonus
        self.transportation_allowance = transportation_allowance
        self.worked_days = worked_days
        self.severance_pay_for_accrued_leave_days = severance_pay_for_accrued_leave_days
        self.int_MONTHS_OF_THE_YEAR = 0.12
        self.int_DAYS_OF_THE_YEAR = 360
        self.int_VACATION_PER_YEAR = 15
        self.int_DAYS_PER_MONTH = 30
        self.int_HALF_A_SEMESTER_WORKED = 2
        self.int_DAYS_WORKED_IN_THE_SEMESTER = 180   