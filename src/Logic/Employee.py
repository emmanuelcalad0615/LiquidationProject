# En este archivo va la inicialización de todas las variables necesarias
class Employee:
    """
    Almacena los datos del empleado a la hora de la indemnizacion y liquidacion
    """

    def __init__(self, basic_salary=0, one_twelfth_vacation_bonus=0, transportation_allowance=0, worked_days=0, severance_pay_for_accrued_leave_days=0):
        self.basic_salary = basic_salary #salario basico
        self.one_twelfth_vacation_bonus = one_twelfth_vacation_bonus # un doceavo de la prima de vacaciones
        self.transportation_allowance = transportation_allowance # auxilio de transporte
        self.worked_days = worked_days # dias trabajados
        self.severance_pay_for_accrued_leave_days = severance_pay_for_accrued_leave_days # dias liquidados de la prima
        self.MONTHS_OF_THE_YEAR = 0.12 # meses del año
        self.DAYS_OF_THE_YEAR = 360 # dias del año
        self.VACATION_PER_YEAR = 15 # vacaciones por año
        self.DAYS_PER_MONTH = 30 # dias por mes
        self.HALF_A_SEMESTER_WORKED = 2 # medio semestre trabajado
        self.DAYS_WORKED_IN_THE_SEMESTER = 180 # dias trabajados en el semestre