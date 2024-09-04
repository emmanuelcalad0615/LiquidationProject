import unittest
from datetime import datetime
from Logic.empleado import Empleado
from Logic.liquidacion import (
    calcular_cesantias,
    intereses,
    calcular_prima_de_servicios,
    vacaciones,
    prima_de_vacaciones,
    verificar_excepciones,
    EmpleadoException,
    ValorNegativo,
    TipoDatosIncorrecto,
    DivisionPorCero,
    NumeroFueraDeRango,
    ValorNoNumerico
)
class LiquidationTest(unittest.TestCase):
    def setUp(self):
        """Configura el estado inicial para cada prueba"""
        self.fecha_inicio = datetime(2019, 10, 28)
        self.fecha_final = datetime(2020, 8, 8)

    def testLiquidation1(self):
        empleado = Empleado(
            salario_basico=5689500,
            un_doceavo_prima_de_vacaciones=5741427,
            auxilio_de_transporte=0,
            dias_trabajados=729,
            dias_liquidados_prima=310,
        )
        valor_esperado=50137036
        try:
            verificar_excepciones(empleado)
            cesantia = calcular_cesantias(empleado)
            interes = intereses(empleado, cesantia)
            prima_servicio = calcular_prima_de_servicios(empleado)
            vacacion = vacaciones(empleado)
            prima_vacacion = prima_de_vacaciones(empleado)

            total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
            self.assertEqual(total_liquidacion, valor_esperado)

        except EmpleadoException as e:
            self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation2(self):
            empleado = Empleado(
                salario_basico=900803,
                un_doceavo_prima_de_vacaciones=0,
                auxilio_de_transporte=80500,
                dias_trabajados=80,
                dias_liquidados_prima=59,
            )
            valor_esperado=584885
            try:
                verificar_excepciones(empleado)
                cesantia = calcular_cesantias(empleado)
                interes = intereses(empleado, cesantia)
                prima_servicio = calcular_prima_de_servicios(empleado)
                vacacion = vacaciones(empleado)
                prima_vacacion = prima_de_vacaciones(empleado)

                total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
                self.assertEqual(total_liquidacion, valor_esperado)

            except EmpleadoException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")
    def testLiquidation3(self):
            empleado = Empleado(
                salario_basico=1450023,
                un_doceavo_prima_de_vacaciones=0,
                auxilio_de_transporte=120018,
                dias_trabajados=169,
                dias_liquidados_prima=30,
            )
            valor_esperado=1590110
            try:
                verificar_excepciones(empleado)
                cesantia = calcular_cesantias(empleado)
                interes = intereses(empleado, cesantia)
                prima_servicio = calcular_prima_de_servicios(empleado)
                vacacion = vacaciones(empleado)
                prima_vacacion = prima_de_vacaciones(empleado)

                total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
                self.assertEqual(total_liquidacion, valor_esperado)

            except EmpleadoException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation4(self):
            empleado = Empleado(
                salario_basico=3638092,
                un_doceavo_prima_de_vacaciones=0,
                auxilio_de_transporte=0,
                dias_trabajados=888,
                dias_liquidados_prima=154,
            )
            valor_esperado=22160507
            try:
                verificar_excepciones(empleado)
                cesantia = calcular_cesantias(empleado)
                interes = intereses(empleado, cesantia)
                prima_servicio = calcular_prima_de_servicios(empleado)
                vacacion = vacaciones(empleado)
                prima_vacacion = prima_de_vacaciones(empleado)

                total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
                self.assertEqual(total_liquidacion, valor_esperado)

            except EmpleadoException as e:



                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation5(self):
        empleado = Empleado(
            salario_basico=5128350,
            un_doceavo_prima_de_vacaciones=854725,
            auxilio_de_transporte=500854,
            dias_trabajados=120,
            dias_liquidados_prima=79,
        )
        valor_esperado = 5380074
        try:
            verificar_excepciones(empleado)
            cesantia = calcular_cesantias(empleado)
            interes = intereses(empleado, cesantia)
            prima_servicio = calcular_prima_de_servicios(empleado)
            vacacion = vacaciones(empleado)
            prima_vacacion = prima_de_vacaciones(empleado)

            total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
            self.assertEqual(total_liquidacion, valor_esperado)

        except EmpleadoException as e:
            self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation6(self):
        empleado = Empleado(
            salario_basico=877803,
            un_doceavo_prima_de_vacaciones=0,
            auxilio_de_transporte=102854,
            dias_trabajados=210,
            dias_liquidados_prima=169,
        )
        valor_esperado=1584510
        try:
            verificar_excepciones(empleado)
            cesantia = calcular_cesantias(empleado)
            interes = intereses(empleado, cesantia)
            prima_servicio = calcular_prima_de_servicios(empleado)
            vacacion = vacaciones(empleado)
            prima_vacacion = prima_de_vacaciones(empleado)

            total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
            self.assertEqual(total_liquidacion, valor_esperado)

        except EmpleadoException as e:



            self.fail(f"Error al calcular la liquidación: {str(e)}")
    # Casos extraordinarios

    def testLiquidation7(self):
            empleado = Empleado(
                salario_basico=5689500,
                un_doceavo_prima_de_vacaciones=0,
                auxilio_de_transporte=0,
                dias_trabajados=999,
                dias_liquidados_prima=999,
            )
            valor_esperado=52622611
            try:
                verificar_excepciones(empleado)
                cesantia = calcular_cesantias(empleado)
                interes = intereses(empleado, cesantia)
                prima_servicio = calcular_prima_de_servicios(empleado)
                vacacion = vacaciones(empleado)
                prima_vacacion = prima_de_vacaciones(empleado)

                total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
                self.assertEqual(total_liquidacion, valor_esperado)

            except EmpleadoException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")


    def testLiquidation8(self):
            empleado = Empleado(
                salario_basico=900803,
                un_doceavo_prima_de_vacaciones=0,
                auxilio_de_transporte=80500,
                dias_trabajados=0,
                dias_liquidados_prima=0,
            )
            valor_esperado=0
            try:
                verificar_excepciones(empleado)
                cesantia = calcular_cesantias(empleado)
                interes = intereses(empleado, cesantia)
                prima_servicio = calcular_prima_de_servicios(empleado)
                vacacion = vacaciones(empleado)
                prima_vacacion = prima_de_vacaciones(empleado)

                total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
                self.assertEqual(total_liquidacion, valor_esperado)

            except EmpleadoException as e:



                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation9(self):
            empleado = Empleado(
                salario_basico=3450023,
                un_doceavo_prima_de_vacaciones=0,
                auxilio_de_transporte=0,
                dias_trabajados=69,
                dias_liquidados_prima=0,
            )
            valor_esperado=1337717
            try:
                verificar_excepciones(empleado)
                cesantia = calcular_cesantias(empleado)
                interes = intereses(empleado, cesantia)
                prima_servicio = calcular_prima_de_servicios(empleado)
                vacacion = vacaciones(empleado)
                prima_vacacion = prima_de_vacaciones(empleado)

                total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
                self.assertEqual(total_liquidacion, valor_esperado)

            except EmpleadoException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation10(self):
            empleado = Empleado(
                salario_basico=26660000,
                un_doceavo_prima_de_vacaciones=0,
                auxilio_de_transporte=0,
                dias_trabajados=0,
                dias_liquidados_prima=0,
            )
            valor_esperado=0
            try:
                verificar_excepciones(empleado)
                cesantia = calcular_cesantias(empleado)
                interes = intereses(empleado, cesantia)
                prima_servicio = calcular_prima_de_servicios(empleado)
                vacacion = vacaciones(empleado)
                prima_vacacion = prima_de_vacaciones(empleado)

                total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
                self.assertEqual(total_liquidacion, valor_esperado)

            except EmpleadoException as e:



                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation11(self):
            empleado = Empleado(
                salario_basico=2230000,
                un_doceavo_prima_de_vacaciones=0,
                auxilio_de_transporte=0,
                dias_trabajados=1,
                dias_liquidados_prima=400,
            )
            valor_esperado=2490168
            try:
                verificar_excepciones(empleado)
                cesantia = calcular_cesantias(empleado)
                interes = intereses(empleado, cesantia)
                prima_servicio = calcular_prima_de_servicios(empleado)
                vacacion = vacaciones(empleado)
                prima_vacacion = prima_de_vacaciones(empleado)

                total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
                self.assertEqual(total_liquidacion, valor_esperado)

            except EmpleadoException as e:



                self.fail(f"Error al calcular la liquidación: {str(e)}")

    def testLiquidation12(self):
            empleado = Empleado(
                salario_basico=4300000,
                un_doceavo_prima_de_vacaciones=0,
                auxilio_de_transporte=0,
                dias_trabajados=1,
                dias_liquidados_prima=1,
            )
            valor_esperado=35836
            try:
                verificar_excepciones(empleado)
                cesantia = calcular_cesantias(empleado)
                interes = intereses(empleado, cesantia)
                prima_servicio = calcular_prima_de_servicios(empleado)
                vacacion = vacaciones(empleado)
                prima_vacacion = prima_de_vacaciones(empleado)

                total_liquidacion = cesantia + interes + prima_servicio + vacacion + prima_vacacion
                self.assertEqual(total_liquidacion, valor_esperado)

            except EmpleadoException as e:
                self.fail(f"Error al calcular la liquidación: {str(e)}")

    # Casos de error
    def testLiquidation13(self):
        """ Salario básico negativo """
        empleado = Empleado(
            salario_basico=-12895,
            un_doceavo_prima_de_vacaciones=0,
            auxilio_de_transporte=5654889,
            dias_trabajados=8,
            dias_liquidados_prima=18,
        )
        with self.assertRaises(ValorNegativo):
            verificar_excepciones(empleado)



    def testLiquidation14(self):
        """ Salario dias trabajados negativo """
        empleado = Empleado(
            salario_basico=-1000000,  # Valor negativo
            un_doceavo_prima_de_vacaciones=50000,
            auxilio_de_transporte=20000,
            dias_trabajados=-30,
            dias_liquidados_prima=10,
        )
        with self.assertRaises(ValorNegativo):
            verificar_excepciones(empleado)

    def testLiquidation15(self):
        """ Días trabajados negativos """
        empleado = Empleado(
            salario_basico=-12895,
            un_doceavo_prima_de_vacaciones=0,
            auxilio_de_transporte=5654889,
            dias_trabajados=8,
            dias_liquidados_prima=18,
        )
        with self.assertRaises(ValorNegativo):
            verificar_excepciones(empleado)

    def testLiquidation16(self):
        """ Salario básico negativo """
        empleado = Empleado(
            salario_basico=-1000000,  # Valor negativo
            un_doceavo_prima_de_vacaciones=50000,
            auxilio_de_transporte=20000,
            dias_trabajados=30,
            dias_liquidados_prima=10,
        )
        with self.assertRaises(ValorNegativo):
            verificar_excepciones(empleado)

    def testLiquidation17(self):
        """ dato incorrecto """
        empleado = Empleado(
            salario_basico="sapo",
            un_doceavo_prima_de_vacaciones=0,
            auxilio_de_transporte=5654889,
            dias_trabajados=8,
            dias_liquidados_prima=18,
        )
        with self.assertRaises(ValorNoNumerico):
            verificar_excepciones(empleado)

    def testLiquidation18(self):
        """ dato incorrecto """
        empleado = Empleado(
            salario_basico=194985,
            un_doceavo_prima_de_vacaciones=0,
            auxilio_de_transporte=5654889,
            dias_trabajados=8,
            dias_liquidados_prima="no me dijieron en la empresa",
        )
        with self.assertRaises(ValorNoNumerico):
            verificar_excepciones(empleado)

    def testLiquidation19(self):
        """ dato incorrecto """
        empleado = Empleado(
            salario_basico=18999,
            un_doceavo_prima_de_vacaciones="soy pobre",
            auxilio_de_transporte=5654889,
            dias_trabajados=8,
            dias_liquidados_prima=18,
        )
        with self.assertRaises(ValorNoNumerico):
            verificar_excepciones(empleado)

    def testLiquidation20(self):
        """ dato incorrecto """
        empleado = Empleado(
            salario_basico="sapo",
            un_doceavo_prima_de_vacaciones=0,
            auxilio_de_transporte="error_data",
            dias_trabajados=8,
            dias_liquidados_prima=18,
        )
        with self.assertRaises(ValorNoNumerico):
            verificar_excepciones(empleado)


if __name__ == "__main__":
    unittest.main()
