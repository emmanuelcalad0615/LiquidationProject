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
        self.months_of_the_year = 0.12
        self.days_of_the_year = 360
        self.vacation_per_year = 15
        self.days_per_month = 30
        self.half_a_semester_worked = 2
        self.days_worked_in_the_semester = 180   