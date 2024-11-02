import sys
import pandas as pd
sys.path.append("src")
from Controller.ControladorUsuarios import EmployeeController  

def initialize_database():
    """Crea la tabla de empleados si no existe en la base de datos."""
    try:
        EmployeeController.create_table()
        print("Tabla de empleados creada o verificada exitosamente.")
    except Exception as e:
        print(f"Error al crear o verificar la tabla: {e}")

def insert_employee():
    """Recoge información del empleado e inserta en la base de datos."""
    print("Ingresa la siguiente información del empleado:")
    document = int(input("Documento del empleado: "))
    name = str(input("Nombre del empleado: "))
    position = str(input("Puesto del empleado: "))
    department = str(input("Departamento del empleado: "))
    hire_date = str(input("Fecha de contratación (YYYY-MM-DD): "))
    contract_type = str(input("Tipo de contrato (fijo_1_año, fijo_inferior_1_año, indefinido): "))
    salary = float(input("Salario del empleado: "))

    EmployeeController.insert_employee(document, name, position, department, hire_date, contract_type, salary)
    print("Empleado insertado correctamente.")

def update_employee():
    """Permite al usuario actualizar información específica de un empleado."""
    document = int(input("Documento del empleado a actualizar: "))
    field = str(input("Campo a actualizar (nombre, puesto, departamento, fecha_contratacion, tipo_contrato, salario): "))
    new_value = str(input("Nuevo valor: "))

    if field == 'salario':
        new_value = float(new_value)

    EmployeeController.update_employee(document, **{field: new_value})
    print("Empleado actualizado correctamente.")

def delete_employee():
    """Elimina un empleado especificado por su documento."""
    document = int(input("Documento del empleado a eliminar: "))
    EmployeeController.delete_employee(document)
    print("Empleado eliminado correctamente.")

def query_employee():
    """Consulta y muestra información de un empleado por su documento."""
    document = int(input("Documento del empleado a consultar: "))
    employee = EmployeeController.get_employee_by_document(document)

    if employee:
        data_series = pd.Series({
            "Documento": employee[1],
            "Nombre": employee[2],
            "Puesto": employee[3],
            "Departamento": employee[4],
            "Fecha de Contratación": employee[5],
            "Tipo de Contrato": employee[6],
            "Salario": employee[7],
            "Estado": employee[8]
        })
        print(data_series)
    else:
        print("No se encontró ningún empleado con ese documento.")



def main():
    initialize_database()
    while True:
        print("""¿Qué acción deseas realizar?:
          1. Insertar Empleado
          2. Actualizar Empleado
          3. Eliminar Empleado
          4. Consultar Empleado
          5. Salir""")
        
        action = input("Elige una opción (1-5): ")
    
        if action == '1':
            insert_employee()
        elif action == '2':
            update_employee()
        elif action == '3':
            delete_employee()
        elif action == '4':
            query_employee()
        elif action == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
