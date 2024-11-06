from flask import Blueprint, render_template, request, redirect, url_for, flash
import sys
sys.path.append("src")
from Controller.ControladorUsuarios import EmployeeController
from Model.Usuario import DuplicateEntryError, DataValidationError, EntryNotFoundError

# Crear el Blueprint llamado 'main_bp'
main_bp = Blueprint('main', __name__, template_folder= 'templates')

# Definir las rutas dentro del Blueprint
@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/acerca')
def acerca():
    return render_template('acerca.html')

@main_bp.route('/como-funciona')
def como_funciona():
    return render_template('como-funciona.html')

@main_bp.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')
@main_bp.route('/crud', methods=['GET', 'POST'])
def crud():
    EmployeeController.create_table()
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            document = request.form['document']
            name = request.form['name']
            position = request.form['position']
            department = request.form['department']
            hire_date = request.form['hire_date']
            contract_type = request.form['contract_type']
            salary = request.form['salary']
            status = request.form['status']

            # Insertar el nuevo empleado usando el controlador
            EmployeeController.insert_employee(
                int(document), name, position, department, hire_date, contract_type, int(salary)
            )

            # Si todo sale bien, mostrar un mensaje de éxito
            flash("Empleado agregado exitosamente.", "success")
            return redirect(url_for('main.crud'))  # Redirigir a la misma página para limpiar el formulario

        except DuplicateEntryError as e:
            # Si ya existe un empleado con el mismo documento
            flash(f"Error: {str(e)}", "danger")
        except DataValidationError as e:
            # Si los datos no son válidos
            flash(f"Error: {str(e)}", "warning")
        except Exception as e:
            # Capturar cualquier otro error
            flash(f"Error al agregar el empleado: {str(e)}", "danger")
    
    # Mostrar el formulario de CRUD cuando se hace un GET o después de un POST exitoso
    return render_template('crud.html')
@main_bp.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    if request.method == 'POST':
        # Obtener el documento del formulario
        document = request.form.get('document')

        try:
            # Llamar al controlador para eliminar el empleado
            EmployeeController.delete_employee(document)
            flash('Empleado eliminado exitosamente', 'success')
        except EntryNotFoundError:
            flash('Empleado no encontrado', 'danger')

        # Redirigir de nuevo al CRUD o página principal
        return redirect(url_for('main.crud'))

    # En el GET, simplemente mostramos el formulario de eliminar
    return render_template('eliminar.html')

@main_bp.route('/editar', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        # Obtener los datos del formulario
        document = request.form.get('document')
        name = request.form.get('name')
        position = request.form.get('position')
        department = request.form.get('department')
        hire_date = request.form.get('hire_date')
        contract_type = request.form.get('contract_type')
        salary = request.form.get('salary')
        status = request.form.get('status')

        # Llamar al controlador para actualizar el empleado
        try:
            EmployeeController.update_employee(
                document, 
                name=name, 
                position=position, 
                department=department, 
                hire_date=hire_date, 
                contract_type=contract_type, 
                salary=salary, 
                status=status
            )
            flash('Empleado actualizado exitosamente', 'success')
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")

        return redirect(url_for('main.crud'))

    # En el GET, mostramos el formulario con los datos actuales del empleado
    document = request.args.get('document')
    employee = EmployeeController.get_employee_by_document(document)
    if not employee:
        flash('Empleado no encontrado', 'danger')
        return redirect(url_for('main.crud'))

    return render_template('editar_empleado.html', employee=employee)

@main_bp.route('/buscar', methods=['GET', 'POST'])
def buscar():
    employee = None  # Inicializamos la variable de employee como None
    if request.method == 'POST':
        # Recuperamos el documento ingresado en el formulario
        document = request.form.get('document')

        if document:
            try:
                # Llamamos al controlador para obtener el empleado por el documento
                employee = EmployeeController.get_employee_by_document(document)
                if not employee:
                    flash('Empleado no encontrado.', 'danger')
            except Exception as e:
                flash(f"Error al buscar el empleado: {str(e)}", 'danger')
        else:
            flash('Por favor, ingresa un documento.', 'warning')

    return render_template('buscar.html', employee=employee)

