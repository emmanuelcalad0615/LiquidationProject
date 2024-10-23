import unittest
import psycopg2
import sys
sys.path.append("src")
sys.path.append("./")   


import unittest
import psycopg2
from src.Controller.ControladorUsuarios import EmployeeController
from src.Controller import SecretConfig

class TestEmployeeController(unittest.TestCase):

    def setUp(self):
        """Crea la tabla antes de cada prueba."""
        EmployeeController.create_employees_table()

    def tearDown(self):
        """Elimina la tabla después de cada prueba."""
        cursor, connection = EmployeeController.get_cursor()
        cursor.execute("DROP TABLE IF EXISTS employees CASCADE;")  
        connection.commit()
        cursor.close()
        connection.close()

    # Pruebas para insert_employee
    def test_insert_employee_valid(self):
        """Prueba de inserción de un empleado con datos válidos."""
        try:
            EmployeeController.insert_employee(1193563677, 'Steven Ceballos', 'Gerente', 'Antioquia', '2020-02-01', 'indefinido', 90000000)
        except Exception as e:
            self.fail(f'Insert valid employee raised an exception {e}')

    def test_insert_employee_duplicate(self):
        """Prueba de inserción de un empleado duplicado."""
        EmployeeController.insert_employee(1193563677, 'Steven Ceballos', 'Gerente', 'Antioquia', '2020-02-01', 'indefinido', 90000000)
        with self.assertRaises(psycopg2.IntegrityError):
            EmployeeController.insert_employee(1193563677, 'Otro Nombre', 'Otro Puesto', 'Otro Departamento', '2021-01-01', 'fijo_1_año', 80000000)

    # Pruebas para update_employee
    def test_update_employee_valid(self):
        """Prueba de actualización válida de un empleado existente."""
        EmployeeController.insert_employee(1193563678, 'Juan Perez', 'Analista', 'Cali', '2021-01-01', 'fijo_1_año', 5000000)
        try:
            EmployeeController.update_employee(1193563678, department='Bogotá')
        except Exception as e:
            self.fail(f'Valid update employee raised an exception {e}')

    def test_update_employee_nonexistent(self):
        """Prueba de actualización de un empleado que no existe."""
        with self.assertRaises(Exception): 
            EmployeeController.update_employee(9999999999, department='Bogotá')

    def test_update_employee_invalid_field(self):
        """Prueba de actualización con un campo que no existe."""
        EmployeeController.insert_employee(1193563679, 'Maria Lopez', 'Desarrolladora', 'Medellín', '2021-05-01', 'indefinido', 6000000)
        with self.assertRaises(Exception):  
            EmployeeController.update_employee(1193563679, invalid_field='valor')

    # Pruebas para delete_employee
    def test_delete_employee_valid(self):
        """Prueba de eliminación de un empleado existente."""
        EmployeeController.insert_employee(1193563680, 'Carlos Ruiz', 'Tester', 'Barranquilla', '2022-03-01', 'fijo_1_año', 4000000)
        try:
            EmployeeController.delete_employee(1193563680)
        except Exception as e:
            self.fail(f'Delete valid employee raised an exception {e}')

    def test_delete_employee_nonexistent(self):
        """Prueba de eliminación de un empleado que no existe."""
        with self.assertRaises(Exception): 
            EmployeeController.delete_employee(9999999999)

    # Pruebas para get_employee_by_document
    def test_query_employee_valid(self):
        """Prueba de consulta de un empleado existente."""
        EmployeeController.insert_employee(1193563681, 'Ana Torres', 'Gerente', 'Cali', '2021-02-01', 'indefinido', 7500000)
        result = EmployeeController.get_employee_by_document(1193563681)
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 1193563681) 

    def test_delete_employee_nonexistent(self):
        """Prueba de eliminación de un empleado que no existe."""
        with self.assertRaises(Exception): 
            EmployeeController.delete_employee(9999999999)

if __name__ == '__main__':
    unittest.main()