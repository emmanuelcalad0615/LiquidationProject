"""
Import necessary modules and classes from Flask and the custom modules for handling business logic.
The Flask `Blueprint` is used to create modular components of the app (routes, views, etc.) that can be registered with the main Flask application.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
import sys
sys.path.append("src")
from Controller.ControladorUsuarios import EmployeeController
from Model.Usuario import DuplicateEntryError, DataValidationError, EntryNotFoundError

"""
Create a Blueprint named 'main_bp'. 
This blueprint contains the routes and views for the web application, and it will be registered to the main Flask app later.
"""
main_bp = Blueprint('main', __name__, template_folder='templates')

"""
Define the routes within this Blueprint. Each route corresponds to a specific page or action within the application.
"""
@main_bp.route('/')
def index():
    """
    The route for the homepage of the application. 
    It renders the 'index.html' template when a GET request is made to the root URL.
    """
    return render_template('index.html')

@main_bp.route('/acerca')
def acerca():
    """
    The route for the 'about us' page.
    It renders the 'acerca.html' template.
    """
    return render_template('acerca.html')

@main_bp.route('/como-funciona')
def como_funciona():
    """
    The route for the 'how it works' page.
    It renders the 'como-funciona.html' template.
    """
    return render_template('como-funciona.html')

@main_bp.route('/calculadora')
def calculadora():
    """
    The route for the 'calculator' page. 
    It renders the 'calculadora.html' template.
    """
    return render_template('calculadora.html')

@main_bp.route('/crud', methods=['GET', 'POST'])
def crud():
    """
    The CRUD page, where new employee records can be added and existing records can be managed.
    - On GET: Displays the CRUD form for adding a new employee.
    - On POST: Handles form submission to insert a new employee.
    """
    EmployeeController.create_table()  # Ensures the employee table is created if it doesn't already exist.

    if request.method == 'POST':
        try:
            # Get form data for the new employee.
            document = request.form['document']
            name = request.form['name']
            position = request.form['position']
            department = request.form['department']
            hire_date = request.form['hire_date']
            contract_type = request.form['contract_type']
            salary = request.form['salary']
            status = request.form['status']

            # Insert the new employee record using the controller.
            EmployeeController.insert_employee(
                int(document), name, position, department, hire_date, contract_type, int(salary)
            )

            # Flash success message if employee is added successfully.
            flash("Empleado agregado exitosamente.", "success")
            return redirect(url_for('main.crud'))  # Redirect to the same page to clear the form.

        except DuplicateEntryError as e:
            # Flash error message if there is a duplicate entry for the employee.
            flash(f"Error: {str(e)}", "danger")
        except DataValidationError as e:
            # Flash warning message if the data entered is invalid.
            flash(f"Error: {str(e)}", "warning")
        except Exception as e:
            # Catch any other general errors.
            flash(f"Error al agregar el empleado: {str(e)}", "danger")

    # Render the 'crud.html' template to show the form after GET or a successful POST.
    return render_template('crud.html')

@main_bp.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    """
    The route for the 'delete' page. 
    - On GET: Displays the delete form.
    - On POST: Handles form submission to delete an employee by their document number.
    """
    if request.method == 'POST':
        # Get the document number from the form.
        document = request.form.get('document')

        try:
            # Call the controller to delete the employee.
            EmployeeController.delete_employee(document)
            flash('Empleado eliminado exitosamente', 'success')
        except EntryNotFoundError:
            flash('Empleado no encontrado', 'danger')

        # Redirect back to the CRUD page or the main page.
        return redirect(url_for('main.crud'))

    # Render the 'eliminar.html' template to show the delete form.
    return render_template('eliminar.html')




@main_bp.route('/buscar', methods=['GET', 'POST'])
def buscar():
    """
    The route for the 'search' page.
    - On GET: Displays an empty search form.
    - On POST: Handles form submission to search for an employee by their document number.
    """
    employee = None  # Initialize the employee variable to None.
    if request.method == 'POST':
        # Get the document entered in the form.
        document = request.form.get('document')

        if document:
            try:
                # Call the controller to search for the employee by document number.
                employee = EmployeeController.get_employee_by_document(document)
                if not employee:
                    flash('Empleado no encontrado.', 'danger')
            except Exception as e:
                flash(f"Error al buscar el empleado: {str(e)}", 'danger')
        else:
            flash('Por favor, ingresa un documento.', 'warning')

    # Render the 'buscar.html' template and pass the employee data if found.
    return render_template('buscar.html', employee=employee)


@main_bp.route('/editar/<document>', methods=['GET', 'POST'])
def editar(document):
    """
    The route for the 'edit employee' page.
    - On GET: Displays the employee's details for editing based on the provided document.
    - On POST: Handles form submission to update the employee's information.
    """
    
    try:
        # If no document is provided, flash an error and redirect to CRUD page
        if not document:
            flash('El documento no ha sido proporcionado', 'danger')
            return redirect(url_for('main.crud'))

        # Try to retrieve the employee using the provided document
        employee = EmployeeController.get_employee_by_document(document)

        # If no employee is found, flash an error and redirect to CRUD page
        if not employee:
            flash('Empleado no encontrado', 'danger')
            return redirect(url_for('main.crud'))

        # Handle the POST request to update employee details
        if request.method == 'POST':
            # Get the form data
            name = request.form.get('name')
            position = request.form.get('position')
            department = request.form.get('department')
            hire_date = request.form.get('hire_date')
            contract_type = request.form.get('contract_type')
            salary = request.form.get('salary')
            status = request.form.get('status')

            try:
                # Attempt to update the employee's data
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
                # If successful, flash a success message and redirect
                flash('Empleado actualizado', 'success')
                return redirect(url_for('main.crud'))

            except Exception as e:
                # If there is an error during update, flash the error message
                flash(f"Error al actualizar el empleado: {str(e)}", 'danger')

        # If it's a GET request, display the employee data in the form
        return render_template('editar.html', employee=employee)

    except Exception as e:
        # This will catch any other unexpected errors (e.g., issues in the GET process)
        flash(f" {str(e)}", 'danger')
        return redirect(url_for('main.crud'))




