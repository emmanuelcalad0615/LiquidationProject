import unittest
import sys
import os
from datetime import date

sys.path.append("src")
sys.path.append("./")   
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Controller.ControladorUsuarios import EmployeeController
from src.Model.Usuario import DataValidationError, EntryNotFoundError, DuplicateEntryError

class TestEmployeeController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Configuración inicial antes de ejecutar todas las pruebas."""
        EmployeeController.drop_table() 
        EmployeeController.create_table()  
    
    def setUp(self):
        """Configuración inicial antes de ejecutar cada prueba."""
        cursor, connection = EmployeeController.get_cursor()
        cursor.execute("DROP TABLE IF EXISTS employees CASCADE;")  
        connection.commit()
        EmployeeController.create_table()  # Crea la tabla después de asegurar que ha sido eliminada
        cursor.close()
        connection.close()

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
            self.fail(f'Insert valid employee raised an exception: {e}')

    def test_insert_employee_duplicate(self):
        """Prueba de inserción de un empleado duplicado."""
        EmployeeController.insert_employee(1193563677, 'Steven Ceballos', 'Gerente', 'Antioquia', '2020-02-01', 'indefinido', 90000000)
        with self.assertRaises(DuplicateEntryError):
            EmployeeController.insert_employee(1193563677, 'Otro Nombre', 'Otro Puesto', 'Otro Departamento', '2021-01-01', 'fijo_1_año', 80000000)

    # Pruebas para update_employee
    def test_update_employee_valid(self):
        """Prueba de actualización válida de un empleado existente."""
        EmployeeController.insert_employee(1193563678, 'Juan Perez', 'Analista', 'Cali', '2021-01-01', 'fijo_1_año', 5000000)
        try:
            EmployeeController.update_employee(1193563678, department='Bogotá')
        except Exception as e:
            self.fail(f'Valid update employee raised an exception: {e}')

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
            self.fail(f'Delete valid employee raised an exception: {e}')

    def test_delete_employee_nonexistent(self):
        """Prueba de eliminación de un empleado que no existe."""
        with self.assertRaises(Exception): 
            EmployeeController.delete_employee(9999999999)

    # Pruebas para get_employee_by_document
    def test_get_employee_by_document_valid(self):
        """Prueba de consulta de un empleado existente."""
        EmployeeController.insert_employee(1193563681, 'Ana Torres', 'Gerente', 'Cali', '2021-02-01', 'indefinido', 7500000)
        result = EmployeeController.get_employee_by_document(1193563681)
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 1193563681)
        
    def test_get_employee_by_document_nonexistent(self):
        """Prueba de consulta de un empleado que no existe."""
        with self.assertRaises(EntryNotFoundError) as context:
            EmployeeController.get_employee_by_document(9999999999)



if __name__ == '__main__':
    unittest.main()
