# Este archivo contiene las pruebas
import unittest
from datetime import datetime
import sys

# Agrega una ruta de Python que debe buscar a los módulos que se importen en el código
sys.path.append("src")

# Las pruebas importan los módulos que hacen el trabajo
from Logic import Liquidation, employee

class LiquidationTest(unittest.TestCase):
    # Cada método de prueba debe llamar un método assert

    # Casos normales
    def testLiquidation1(self):
        basic_salary = 5689500
        vacation_bonus = 5741427
        auxilio_t = 0
        dias_t = 729
        dias_lp = 310
        dias_v = 28
        fecha_i = datetime(2019,10,28)
        fecha_f = datetime(2020,8,8)
        tipo_contrato = 3
        motivo_finalizacion = 4
        total_liquidacion = 30741427
        resultado = Liquidation.employee.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation2(self):
        basic_salary = 900803
        vacation_bonus = 160825
        auxilio_t = 80500
        dias_t = 80
        dias_lp = 59
        dias_v = 7
        fecha_i = datetime(2019,3,28)
        fecha_f = datetime(2019,7,16)
        tipo_contrato = 3
        motivo_finalizacion = 2
        total_liquidacion = 584886
        resultado = Liquidation.Empleados.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation3(self):
        basic_salary = 1450023
        vacation_bonus = 340353
        auxilio_t = 120018
        dias_t = 169
        dias_lp = 30
        dias_v = 20
        fecha_i = datetime(2018,1,14)
        fecha_f = datetime(2018,8,8)
        tipo_contrato = 2
        motivo_finalizacion = 4
        total_liquidacion = 1590109
        resultado = Liquidation.Empleados.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation4(self):
        basic_salary = 3638092
        vacation_bonus = 4486980
        auxilio_t = 0
        dias_t = 888
        dias_lp = 154
        dias_v = 16
        fecha_i = datetime(2021,12,17)
        fecha_f = datetime(2024,6,4)
        tipo_contrato = 1
        motivo_finalizacion = 2
        total_liquidacion = 22160508
        resultado = Liquidation.Empleados.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)
    
    def testLiquidation5(self):
        basic_salary = 5128350
        vacation_bonus = 854725
        auxilio_t = 500854
        dias_t = 120
        dias_lp = 79
        dias_v = 15
        fecha_i = datetime(2015,1,15)
        fecha_f = datetime(2015,7,28)
        tipo_contrato = 1
        motivo_finalizacion = 1
        total_liquidacion = 4896205
        resultado = Liquidation.Empleados.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation6(self):
        basic_salary = 877803
        vacation_bonus = 256026
        auxilio_t = 102854
        dias_t = 210
        dias_lp = 169
        dias_v = 21
        fecha_i = datetime(2011,1,14)
        fecha_f = datetime(2011,12,7)
        tipo_contrato = 3
        motivo_finalizacion = 2
        total_liquidacion = 1584509
        resultado = Liquidation.Empleados.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    # Casos extraordinarios
    def testLiquidation7(self): 
        """ Días trabajados y días de prima exagerados """  
        basic_salary = 5689500
        vacation_bonus = 7894181
        auxilio_t = 0
        dias_t = 999
        dias_lp = 999
        dias_v = 15
        fecha_i = datetime(2019,11,25)
        fecha_f = datetime(2020,6,5)
        tipo_contrato = 2
        motivo_finalizacion = 2
        total_liquidacion = 52622612
        resultado = Liquidation.Empleados.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation8(self):
        """ Despido del día después de trabajo"""   
        basic_salary = 900803
        vacation_bonus = 0
        auxilio_t = 80500
        dias_t = 1
        dias_lp = 1
        dias_v = 15
        fecha_i = datetime(2019,3,28)
        fecha_f = datetime(2019,3,29)
        tipo_contrato = 3
        motivo_finalizacion = 3
        total_liquidacion = 7955
        resultado = Liquidation.Empleados.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation9(self):
        """ Prima liquidada cero"""   
        basic_salary = 3450023
        vacation_bonus = 0
        auxilio_t = 0
        dias_t = 69
        dias_lp = 0
        dias_v = 15
        fecha_i = datetime(2019,1,28)
        fecha_f = datetime(2019,8,7)
        tipo_contrato = 3
        motivo_finalizacion = 1
        total_liquidacion = 1337718
        resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation10(self): 
        """ Despido al mismo día de comienzo de trabajo """  
        basic_salary = 26660000
        vacation_bonus = 0
        auxilio_t = 0
        dias_t = 0
        dias_lp = 0
        dias_v = 15
        fecha_i = datetime(2021,12,17)
        fecha_f = datetime(2021,12,21)
        tipo_contrato = 1
        motivo_finalizacion = 2
        total_liquidacion = 0
        resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation11(self):  
        """ Muchos días de vacaciones acumulados""" 
        basic_salary = 2230000
        vacation_bonus = 180000
        auxilio_t = 0
        dias_t = 200
        dias_lp = 200
        dias_v = 100
        fecha_i = datetime(2019,12,18)
        fecha_f = datetime(2022,7,28)
        tipo_contrato = 3
        motivo_finalizacion = 1
        total_liquidacion = 2490169
        resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation12(self): 
        """ Despido a los 15 días sin liquidación"""  
        basic_salary = 4300000
        vacation_bonus = 100000
        auxilio_t = 100000
        dias_t = 1
        dias_lp = 1
        dias_v = 15
        fecha_i = datetime(2020,1,14)
        fecha_f = datetime(2020,1,29)
        tipo_contrato = 1
        motivo_finalizacion = 2
        total_liquidacion = 35837
        resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    
    # Casos de error
    def testliquidation13(self):
        """ basic_salary negativo """
        basic_salary= -895516
        auxilio_t=5654889
        dias_t=156
        dias_lp= 18
        dias_v= 12
        fecha_i= datetime(2019, 1,25)
        fecha_f= datetime(2019, 12, 31)
        tipo_contrato= 2
        motivo_finalizacion= 3
        
        try:
            resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.basic_salaryNegativo  :
            pass  # Forzar Exito

    def testliquidation14(self):
        """ fecha incorrecta """
        basic_salary = 12895516
        auxilio_t=5654889
        dias_t=156
        dias_lp= 18
        dias_v= 20
        fecha_i=datetime(2019, 18,25)
        fecha_f=datetime(2019, 12, 31)
        tipo_contrato=2
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos( basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.FechaIncorrecta  :
            pass  # Forzar Exito

    def testliquidation15(self):
        """ dias trabajados negativos """
        basic_salary = 12895
        auxilio_t=5654889
        dias_t=-8
        dias_lp= 18
        dias_v= 48
        fecha_i=datetime(2019, 9,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato=2
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.DiasNegativos  :
            pass  # Forzar Exito

    def testliquidation16(self):
        """ dias prima negativos """
        basic_salary = 18492
        auxilio_t = 0
        dias_t=8
        dias_lp= -1
        dias_v= 2
        fecha_i=datetime(2010, 9,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato= 2
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.DiasNegativos  :
            pass  # Forzar Exito

    def testliquidation17(self):
        """ dias vacaciones negativos """
        basic_salary= 18492
        auxilio_t = 0
        dias_t=8
        dias_lp= 18
        dias_v= -28
        fecha_i=datetime(2010, 9,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato=2
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.DiasNegativos  :
            pass  # Forzar Exito

    def testliquidation18(self):
        """ tipo de contrato se sale del rango """
        basic_salary= 18492
        auxilio_t = 0
        dias_t=8
        dias_lp= 19
        dias_v= 20
        fecha_i=datetime(2012, 9,26)
        fecha_f=datetime(20, 12, 31)
        tipo_contrato=5
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.FueradeRango :
            pass  # Forzar Exito

    def testliquidation19(self):
        """ motivo de finalizacion fuera de rango """
        basic_salary= 18492
        auxilio_t = 0
        dias_t=8
        dias_lp= 19
        dias_v= 2
        fecha_i=datetime(2020, 11,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato=2
        motivo_finalizacion=18
        
        try:
            resultado = Liquidation.Empleado.calculos( basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.Fueraderango  :
            pass  # Forzar Exito

    def testliquidation20(self):
        """ coloca un string cuando era un entero"""
        basic_salary= 1849879
        auxilio_t = 0
        dias_t="hola soy pobre"
        dias_lp= 19
        dias_v= 2
        fecha_i=datetime(2020, 11,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato=3
        motivo_finalizacion=1
        
        try:
            resultado = Liquidation.Empleado.calculos(basic_salary,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.valorincorrecto  :
            pass  # Forzar Exito

