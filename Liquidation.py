# Este archivo contiene toda la lógica del programa
"""
Nombres de las variables
salario : salario básico
prima de vacaciones :  prima_v
auxilio transporte : auxilio_t
días trabajados : días_t
intereses cesantías : interes_c
prima servicios : prima_s
días liquidados prima : dias_lp
indemnizacion(por contrato a 1 año) : indem_1
indemnizacion(por contrato a menos de 1 año) : indem_2
indemnizacion(por contrato a termino indefinido) : indem_3
dias faltantes del contrato : dias_f
meses de contrato cumplido : meses_c.
dias faltantes del mes(con respecto al contrato) : dias_fm
ingreso en UVT : ingreso_uvt
porcentaje con respecto al ingreso de uvt : porcentaje_uvt
porcentaje de retencion : porcentaje_r
"""
class EmpleadoException(Exception):
    """Clase base para excepciones relacionadas con la clase Empleado."""

class ValorNegativo(Exception):
    """Excepción para valores negativos."""
    pass

class TipoDatosIncorrecto(Exception):
    """Excepción para tipos de datos incorrectos."""
    pass

class DivisionPorCero(Exception):
    """Excepción para divisiones por cero."""
    pass

class NumeroFueraDeRango(Exception):
    """Excepción para números fuera de rango."""
    pass

class Empleado:

    def __init__(self, salario, prima_v, auxilio_t, dias_t, dias_lp, dias_f, meses_c, dias_fm, porcentaje_uvt, porcentaje_r, tipo_contrato):
        self.salario = salario
        self.prima_v = prima_v
        self.auxilio_t = auxilio_t
        self.dias_t = dias_t
        self.dias_lp = dias_lp
        self.dias_f = dias_f
        self.meses_c = meses_c
        self.dias_fm = dias_fm
        self.porcentaje_uvt = porcentaje_uvt
        self.porcentaje_r = porcentaje_r
        self.tipo_contrato = tipo_contrato

    def calcular_cesantias(self, salario, prima_v, auxilio_t, dias_t):
        if dias_t <= 0:
            raise ValorNegativo("Los días trabajados deben ser mayores que cero.")
        try:
            cesantias = (salario + (1/12) * prima_v + auxilio_t) / (366 * dias_t)
        except ZeroDivisionError:
            raise DivisionPorCero() from None
        return cesantias

    def calcular_intereses(self, cesantias, dias_t):
        if cesantias <= 0:
            raise ValorNegativo("Las cesantías deben ser mayores que cero.")
        try:
            interes_c = (cesantias * 0.12) / 366 * dias_t
        except ZeroDivisionError:
            raise DivisionPorCero() from None
        return interes_c
    
    def calcular_prima_servicios(self, salario, prima_v, auxilio_t, dias_lp):
        if dias_lp <= 0:
            raise ValorNegativo("Los días de licencia pagada deben ser mayores que cero.")
        try:
            prima_s = ((salario + (1/12 * prima_v) + auxilio_t) / 2) / (180 * dias_lp)
        except ZeroDivisionError:
            raise DivisionPorCero() from None
        return prima_s

    def calcular_prima_vacaciones(self, salario, dias_t):
        if dias_t <= 0:
            raise ValorNegativo("Los días trabajados deben ser mayores que cero.")
        try:
            prima_v = (salario / 30) * (dias_t * 15 / 360)
        except ZeroDivisionError:
            raise DivisionPorCero() from None
        return prima_v

    def calcular_retencion(self, ingreso_uvt, porcentaje_uvt, porcentaje_r, salario):
        if self.salario > 3900000:
            ingreso_uvt = (salario / 42.412)
            retencion = (ingreso_uvt - porcentaje_uvt) * porcentaje_r
        else:
            print("El trabajador no debe pagar retención a la fuente")
            return 0


    def calculos(self, salario, prima_v, auxilio_t, dias_t, dias,lp, dias_f, meses_c, dias_fm, porcentaje_uvt, porcentaje_r,dias_lp,tipo_contrato,ingreso_uvt):
        cesantias = self.calcular_cesantias(salario,prima_v,auxilio_t, dias_t)
        intereses_c = self.calcular_intereses(cesantias,dias_t)
        prima_s = self.calcular_prima_servicios(salario,prima_v,auxilio_t,dias_lp)
        indem = self.calcular_indemnizacion(salario,dias_f,meses_c,dias_fm,tipo_contrato)
        retencion = self.calcular_retencion(ingreso_uvt,porcentaje_uvt,porcentaje_r,salario)


        resultado_final = {
            'cesantias': cesantias,
            'intereses_c': intereses_c,
            'prima_s': prima_s,
            'indemnizacion': indem,
            'retencion': retencion
        }

        return resultado_final
