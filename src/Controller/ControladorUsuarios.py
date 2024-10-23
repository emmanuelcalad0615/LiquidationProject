import sys
import psycopg2
sys.path.append("src")
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
    def create_employees_table():
        """Crea la tabla de empleados en la base de datos si no existe."""
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
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def insert_employee(document, name, position, department, hire_date, contract_type, salary):
        """Inserta un nuevo empleado en la tabla 'employees'."""
        # Verifica si el documento ya existe antes de insertar
        EmployeeInput.check_primary_key(document, EmployeeController.get_employee_by_document)

        # Crea una instancia de EmployeeInput y valida los datos
        employee_input = EmployeeInput(document, name, position, department, hire_date, contract_type, salary)
        employee_input.validate()

        cursor, connection = EmployeeController.get_cursor()
        try:
            cursor.execute("""
                INSERT INTO employees (document, name, position, department, hire_date, contract_type, salary) 
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, (document, name, position, department, hire_date, contract_type, salary))
            connection.commit()
            print(f"Empleado '{name}' insertado correctamente.")
        except psycopg2.IntegrityError as e:
            connection.rollback()  
            raise DuplicateEntryError("Entrada duplicada para el documento.") 
        except Exception as e:
            print(f"Error al insertar empleado: {e}")
            raise e 
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update_employee(employee_document, **kwargs):
        """Actualiza los datos de un empleado en la tabla 'employees'."""
        cursor, connection = EmployeeController.get_cursor()
        
        set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        values = list(kwargs.values())

        try:
            cursor.execute(f"""
                UPDATE employees SET {set_clause} WHERE document = %s;
            """, (*values, employee_document))
            
            if cursor.rowcount == 0:
                raise EntryNotFoundError("Empleado no encontrado para actualizar.")
                
            connection.commit()
            print(f"Empleado con documento '{employee_document}' actualizado correctamente.")
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            raise e  
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_employee(employee_document):
        """Elimina un empleado de la tabla 'employees'."""
        cursor, connection = EmployeeController.get_cursor()
        
        try:
            cursor.execute("DELETE FROM employees WHERE document = %s;", (employee_document,))
            
            if cursor.rowcount == 0:
                raise EntryNotFoundError("Empleado no encontrado para eliminar.")
                
            connection.commit()
            print(f"Empleado con documento '{employee_document}' eliminado correctamente.")
        except Exception as e:
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
                raise EntryNotFoundError("Empleado no encontrado.")
                
            return employee
        except Exception as e:
            print(f"Error al consultar empleado: {e}")
            return None
        finally:
            cursor.close()
            connection.close()