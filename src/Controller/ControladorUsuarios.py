import sys
import psycopg2
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controller import SecretConfig
from Model.Usuario import EmployeeInput, DuplicateEntryError, EntryNotFoundError, DataValidationError

class EmployeeController:
    
    @staticmethod
    def get_cursor():
        """Crea una conexión a la base de datos y retorna un cursor para ejecutar consultas."""
        try:
            connection = psycopg2.connect(
                database=SecretConfig.PGDATABASE,
                user=SecretConfig.PGUSER,
                password=SecretConfig.PGPASSWORD,
                host=SecretConfig.PGHOST,
                port=SecretConfig.PGPORT
            )
            return connection.cursor(), connection  
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise e

    @staticmethod
    def drop_table():
        """Elimina la tabla de empleados si existe."""
        cursor, connection = EmployeeController.get_cursor()
        try:
            cursor.execute("DROP TABLE IF EXISTS employees;")
            connection.commit()
            print("Tabla 'employees' eliminada con éxito.")
        except Exception as e:
            print(f"Error al eliminar la tabla 'employees': {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create_table():
        """Crea la tabla de empleados."""
        cursor, connection = EmployeeController.get_cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    document BIGINT UNIQUE NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    position VARCHAR(50),
                    department VARCHAR(50),
                    hire_date DATE,
                    contract_type VARCHAR(50),
                    salary FLOAT,
                    status VARCHAR(20) DEFAULT 'active'
                );
            """)
            connection.commit()
            print("Tabla 'employees' creada con éxito.")
        except Exception as e:
            print(f"Error al crear la tabla 'employees': {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def insert_employee(document, name, position, department, hire_date, contract_type, salary):
        """Inserta un nuevo empleado en la tabla 'employees'."""
        employee_input = EmployeeInput(document, name, position, department, hire_date, contract_type, salary)
        employee_input.validate()
        
        try:
            EmployeeController.get_employee_by_document(document)
            raise DuplicateEntryError(f"Ya existe un empleado con el documento {document}.")
        except EntryNotFoundError:
            pass  
        cursor, connection = EmployeeController.get_cursor()
        try:
            cursor.execute("""
                INSERT INTO employees (document, name, position, department, hire_date, contract_type, salary) 
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, (document, name, position, department, hire_date, contract_type, salary))
            connection.commit()
            print(f"Empleado '{name}' insertado correctamente.")
        except psycopg2.IntegrityError:
            connection.rollback()
            raise DuplicateEntryError(f"Ya existe un empleado con el documento {document}.")
        except Exception as e:
            connection.rollback()
            print(f"Error al insertar empleado: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update_employee(document, **kwargs):
        """Actualiza los datos de un empleado en la tabla 'employees'."""
        EmployeeController.get_employee_by_document(document)

        cursor, connection = EmployeeController.get_cursor()
        
        valid_fields = {
            'name': 'name',
            'position': 'position',
            'department': 'department',
            'hire_date': 'hire_date',
            'contract_type': 'contract_type',
            'salary': 'salary'
        }
        
        update_fields = {}
        for key, value in kwargs.items():
            if key in valid_fields:
                update_fields[valid_fields[key]] = value

        if not update_fields:
            raise ValueError("No hay campos válidos para actualizar.")

        set_clause = ", ".join([f"{key} = %s" for key in update_fields.keys()])
        values = list(update_fields.values())
        values.append(document)

        try:
            cursor.execute(f"""
                UPDATE employees 
                SET {set_clause} 
                WHERE document = %s;
            """, values)
            
            connection.commit()
            print(f"Empleado con documento '{document}' actualizado correctamente.")
        except Exception as e:
            connection.rollback()
            print(f"Error al actualizar empleado: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_employee(document):
        """Elimina un empleado de la tabla 'employees'."""
        EmployeeController.get_employee_by_document(document)
        
        cursor, connection = EmployeeController.get_cursor()
        try:
            cursor.execute("DELETE FROM employees WHERE document = %s;", (document,))
            connection.commit()
            print(f"Empleado con documento '{document}' eliminado correctamente.")
        except Exception as e:
            connection.rollback()
            print(f"Error al eliminar empleado: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_employee_by_document(document):
        """Consulta un empleado por su documento y devuelve sus datos."""
        cursor, connection = EmployeeController.get_cursor()
        try:
            cursor.execute("SELECT * FROM employees WHERE document = %s;", (document,))
            employee = cursor.fetchone()
            
            if not employee:
                raise EntryNotFoundError(f"No se encontró empleado con documento {document}.")
                
            return employee
        except EntryNotFoundError as e:
            raise e
        except Exception as e:
            print(f"Error al consultar empleado: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()