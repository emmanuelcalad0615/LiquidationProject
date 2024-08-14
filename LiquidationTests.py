# Este archivo contiene las pruebas
import unittest
from datetime import datetime

class LiquidationTest(unittest.TestCase):
    # Cada método de prueba debe llamar un método assert

    # Casos normales

    def testLiquidation1(self):
        salario = 5,689.500
        prima_v = 5,741.427
        auxilio_t = 0
        dias_t = 729
        dias_lp = 310
        dias_v = 28
        fecha_i = datetime(2019,10,28)
        fecha_f = datetime(2020,8,8)
        tipo_contrato = 3
        motivo_finalizacion = 4
        total_liquidacion = 30,741.427
        resultado = Liquidation.Empleados.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation2(self):
        salario = 900.803
        prima_v = 160.825
        auxilio_t = 80.500
        dias_t = 80
        dias_lp = 59
        dias_v = 7
        fecha_i = datetime(2019,3,28)
        fecha_f = datetime(2019,7,16)
        tipo_contrato = 3
        motivo_finalizacion = 2
        total_liquidacion = 584.886
        resultado = Liquidation.Empleados.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation3(self):
        salario = 1,450.023
        prima_v = 340.353
        auxilio_t = 120.018
        dias_t = 169
        dias_lp = 30
        dias_v = 20
        fecha_i = datetime(2018,1,14)
        fecha_f = datetime(2018,8,8)
        tipo_contrato = 2
        motivo_finalizacion = 4
        total_liquidacion = 1,590.109
        resultado = Liquidation.Empleados.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation4(self):
        salario = 3,638.092
        prima_v = 4,486.980
        auxilio_t = 0
        dias_t = 888
        dias_lp = 154
        dias_v = 16
        fecha_i = datetime(2021,12,17)
        fecha_f = datetime(2024,6,4)
        tipo_contrato = 1
        motivo_finalizacion = 2
        total_liquidacion = 22,160.508
        resultado = Liquidation.Empleados.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)
    
    def testLiquidation5(self):
        salario = 5,128.350
        prima_v = 854.725
        auxilio_t = 500.854
        dias_t = 120
        dias_lp = 79
        dias_v = 15
        fecha_i = datetime(2015,1,15)
        fecha_f = datetime(2015,7,28)
        tipo_contrato = 1
        motivo_finalizacion = 1
        total_liquidacion = 4,896.205
        resultado = Liquidation.Empleados.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation6(self):
        salario = 877.803
        prima_v = 256.026
        auxilio_t = 102.854
        dias_t = 210
        dias_lp = 169
        dias_v = 21
        fecha_i = datetime(2011,1,14)
        fecha_f = datetime(2011,12,7)
        tipo_contrato = 3
        motivo_finalizacion = 2
        total_liquidacion = 1,584.509
        resultado = Liquidation.Empleados.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    # Casos excepcionales
    def testLiquidation7(self):   
        salario = 5,689.500
        prima_v = 7,894.181
        auxilio_t = 0
        dias_t = 999
        dias_lp = 999
        dias_v = 15
        fecha_i = datetime(2019,11,25)
        fecha_f = datetime(2020,6,5)
        tipo_contrato = 2
        motivo_finalizacion = 2
        total_liquidacion = 52,622.612
        resultado = Liquidation.Empleados.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation8(self):   
        salario = 900,803
        prima_v = 0
        auxilio_t = 80,500
        dias_t = 1
        dias_lp = 1
        dias_v = 15
        fecha_i = datetime(2019,3,28)
        fecha_f = datetime(2019,3,29)
        tipo_contrato = 3
        motivo_finalizacion = 3
        total_liquidacion = 7,955
        resultado = Liquidation.Empleados.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation9(self):   
        salario = 3,450.023
        prima_v = 0
        auxilio_t = 0
        dias_t = 69
        dias_lp = 0
        dias_v = 15
        fecha_i = datetime(2019,1,28)
        fecha_f = datetime(2019,8,7)
        tipo_contrato = 3
        motivo_finalizacion = 1
        total_liquidacion = 1,337.718
        resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation10(self):   
        salario = 26,660.000
        prima_v = 0
        auxilio_t = 0
        dias_t = 0
        dias_lp = 0
        dias_v = 15
        fecha_i = datetime(2021,12,17)
        fecha_f = datetime(2021,12,21)
        tipo_contrato = 1
        motivo_finalizacion = 2
        total_liquidacion = 0
        resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation11(self):   
        salario = 2,230.000
        prima_v = 180.000
        auxilio_t = 0
        dias_t = 20
        dias_lp = 20
        dias_v = 100
        fecha_i = datetime(2019,12,18)
        fecha_f = datetime(2022,7,28)
        tipo_contrato = 3
        motivo_finalizacion = 1
        total_liquidacion = 2,490.169
        resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    def testLiquidation12(self):   
        salario = 4,300.000
        prima_v = 100.000
        auxilio_t = 100.000
        dias_t = 1
        dias_lp = 1
        dias_v = 15
        fecha_i = datetime(2020,1,14)
        fecha_f = datetime(2020,1,29)
        tipo_contrato = 1
        motivo_finalizacion = 2
        total_liquidacion = 35.837
        resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
        self.assertEqual( total_liquidacion,resultado)

    
    # Casos de error
    def testliquidation13(self):
        """ salario negativo """
        salario= -895516
        auxilio_t=5654889
        dias_t=156
        dias_lp= 18
        dias_v= 12
        fecha_i= datetime(2019, 1,25)
        fecha_f= datetime(2019, 12, 31)
        tipo_contrato= 2
        motivo_finalizacion= 3
        
        try:
            resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.SalarioNegativo  :
            pass  # Forzar Exito

    def testliquidation14(self):
        """ fecha incorrecta """
        salario = 12895516
        auxilio_t=5654889
        dias_t=156
        dias_lp= 18
        dias_v= 20
        fecha_i=datetime(2019, 18,25)
        fecha_f=datetime(2019, 12, 31)
        tipo_contrato=2
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos( salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion)
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.FechaIncorrecta  :
            pass  # Forzar Exito

    def testliquidation15(self):
        """ dias trabajados negativos """
        salario = 12895
        auxilio_t=5654889
        dias_t=-8
        dias_lp= 18
        dias_v= 48
        fecha_i=datetime(2019, 9,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato=2
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.DiasNegativos  :
            pass  # Forzar Exito

    def testliquidation16(self):
        """ dias prima negativos """
        salario = 18492
        auxilio_t = 0
        dias_t=8
        dias_lp= -1
        dias_v= 2
        fecha_i=datetime(2010, 9,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato= 2
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.DiasNegativos  :
            pass  # Forzar Exito

    def testliquidation17(self):
        """ dias vacaciones negativos """
        salario= 18492
        auxilio_t = 0
        dias_t=8
        dias_lp= 18
        dias_v= -28
        fecha_i=datetime(2010, 9,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato=2
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.DiasNegativos  :
            pass  # Forzar Exito

    def testliquidation18(self):
        """ tipo de contrato se sale del rango """
        salario= 18492
        auxilio_t = 0
        dias_t=8
        dias_lp= 19
        dias_v= 20
        fecha_i=datetime(2012, 9,26)
        fecha_f=datetime(20, 12, 31)
        tipo_contrato=5
        motivo_finalizacion=3
        
        try:
            resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.FueradeRango :
            pass  # Forzar Exito

    def testliquidation19(self):
        """ motivo de finalizacion fuera de rango """
        salario= 18492
        auxilio_t = 0
        dias_t=8
        dias_lp= 19
        dias_v= 2
        fecha_i=datetime(2020, 11,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato=2
        motivo_finalizacion=18
        
        try:
            resultado = Liquidation.Empleado.calculos( salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.Fueraderango  :
            pass  # Forzar Exito

    def testliquidation20(self):
        """ coloca un string cuando era un entero"""
        salario= 1849879
        auxilio_t = 0
        dias_t="hola soy pobre"
        dias_lp= 19
        dias_v= 2
        fecha_i=datetime(2020, 11,26)
        fecha_f=datetime(2021, 12, 31)
        tipo_contrato=3
        motivo_finalizacion=1
        
        try:
            resultado = Liquidation.Empleado.calculos(salario,auxilio_t,dias_t,dias_lp,dias_v,fecha_i,fecha_f,tipo_contrato,motivo_finalizacion )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( resultado, 0 )  # Forzar fallo caso
        except  Liquidation.Empleado.valorincorrecto  :
            pass  # Forzar Exito

