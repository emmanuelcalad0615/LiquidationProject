import sys
sys.path.append("src")

# Definición de excepciones personalizadas
class DuplicateEntryError(Exception):
    """Excepción para entradas duplicadas en la base de datos."""
    pass

class EntryNotFoundError(Exception):
    """Excepción para búsquedas de entradas que no existen en la base de datos."""
    pass

class DataValidationError(Exception):
    """Excepción para datos de entrada inválidos."""
    pass

# Clase para manejar la entrada de empleado
class EmployeeInput:
    def __init__(self, document, name, position, department, hire_date, contract_type, salary):
        self.document = document
        self.name = name
        self.position = position
        self.department = department
        self.hire_date = hire_date
        self.contract_type = contract_type
        self.salary = salary

    def validate(self):
        if not all([self.document, self.name, self.position, self.department, self.hire_date, self.contract_type, self.salary]):
            raise DataValidationError("Todos los campos son requeridos.")
        
        if self.contract_type not in ['fijo_1_año', 'fijo_inferior_1_año', 'indefinido']:
            raise DataValidationError("Tipo de contrato inválido. Debe ser 'fijo_1_año', 'fijo_inferior_1_año' o 'indefinido'.")

        if not isinstance(self.salary, (int, float)) or self.salary < 0:
            raise DataValidationError("El salario debe ser un número positivo.")

    # Validación de existencia utilizando una función externa de verificación
    @staticmethod
    def check_primary_key(document, db_check_func):
        if db_check_func(document):
            raise DuplicateEntryError(f"Ya existe un empleado con el documento {document}.")

# Clase para manejar la salida de empleado
class EmployeeOutput:
    @staticmethod
    def validate_employee_found(found, operation):
        if not found:
            raise EntryNotFoundError(f"Empleado no encontrado para la operación: {operation}.")