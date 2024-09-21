from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import os
import sys
sys.path.append("src")

# Importar los módulos necesarios
from Logic.employee import Employee
from Logic.Liquidation import (
    calculate_severance_pay_amount,
    calculate_severance_pay_interest,
    calculate_service_bonus,
    calculate_vacation,
    verify_exceptions,  
    EmployeeException,
    NegativeValueError,
    IncorrectDataTypeError,
    DivisionByZeroError,
    NumberOutOfRangeError
)
from Logic.Compensation import calculate_compensation

# Definir variables globales de fuente
FONT_NAME = 'Londona-reguler.otf'  # Cambia esto por la ruta a tu archivo .ttf
FONT_SIZE = '30sp'  # Tamaño de la fuente para todos los textos

# Pantalla de bienvenida
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        welcome_label = Label(text="Bienvenido al Programa de Liquidación", font_size=FONT_SIZE, font_name=FONT_NAME)
        start_button = Button(text="Iniciar", size_hint=(1, 0.2), font_size=FONT_SIZE, font_name=FONT_NAME)
        start_button.bind(on_release=self.go_to_data)
        
        layout.add_widget(welcome_label)
        layout.add_widget(start_button)
        self.add_widget(layout)

    def go_to_data(self, *args):
        self.manager.current = 'data'

# Screen for employee data
class EmployeeDataScreen(Screen):
    def __init__(self, **kwargs):
        super(EmployeeDataScreen, self).__init__(**kwargs)
        self.layout = GridLayout(cols=2, padding=10, spacing=10)
        
        self.layout.add_widget(Label(text="Salario Básico Mensual:", font_size=FONT_SIZE, font_name=FONT_NAME))
        self.salary_input = TextInput(multiline=False, font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(self.salary_input)
        
        self.layout.add_widget(Label(text="Auxilio de Transporte:", font_size=FONT_SIZE, font_name=FONT_NAME))
        self.transport_input = TextInput(multiline=False, font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(self.transport_input)
        
        self.layout.add_widget(Label(text="Días Trabajados:", font_size=FONT_SIZE, font_name=FONT_NAME))
        self.days_input = TextInput(multiline=False, font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(self.days_input)
        
        submit_button = Button(text="Calcular Liquidación", font_size=FONT_SIZE, font_name=FONT_NAME)
        submit_button.bind(on_release=self.calculate_liquidation)
        self.layout.add_widget(submit_button)
        
        self.add_widget(self.layout)
    
    def calculate_liquidation(self, *args):
        try:
            basic_monthly_salary = float(self.salary_input.text)
            transportation_allowance = float(self.transport_input.text)
            worked_days = int(self.days_input.text)

            employee = Employee(
                basic_monthly_salary=basic_monthly_salary,
                transportation_allowance=transportation_allowance,
                worked_days=worked_days,
            )
            
            # Verifying exceptions
            verify_exceptions(employee)
            
            # Saving the employee in the instance of the screen manager
            self.manager.employee = employee
            self.manager.current = 'result'
            
        except (NegativeValueError, IncorrectDataTypeError, DivisionByZeroError, NumberOutOfRangeError) as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error al crear el objeto empleado: {str(e)}")

# Screen for showing liquidation results
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.result_label = Label(text="Resultados de la Liquidación", font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(self.result_label)
        
        self.liquidation_details = Label(text="", font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(self.liquidation_details)
        
        # Layout for the buttons at the bottom
        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)
        
        back_button = Button(text="Volver", font_size=FONT_SIZE, font_name=FONT_NAME)
        back_button.bind(on_release=self.go_back)
        button_layout.add_widget(back_button)
        
        compensation_button = Button(text="Escoger Indemnización", font_size=FONT_SIZE, font_name=FONT_NAME)
        compensation_button.bind(on_release=self.go_to_compensation)
        button_layout.add_widget(compensation_button)
        
        self.layout.add_widget(button_layout)
        
        self.add_widget(self.layout)
    
    def on_enter(self, *args):
        employee = self.manager.employee
        
        try:
            # Calculate the different components of the liquidation
            severance_pay = calculate_severance_pay_amount(employee)
            severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
            service_bonus = calculate_service_bonus(employee)
            vacation = calculate_vacation(employee)
            
            total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation

            # Showing results
            results = (f"Cesantías: {severance_pay}\n"
                       f"Intereses de cesantías: {severance_pay_interest}\n"
                       f"Prima de servicios: {service_bonus}\n"
                       f"Vacaciones: {vacation}\n"
                       f"\nLiquidación total: {total_liquidation}")
            
            self.liquidation_details.text = results

        except EmployeeException as e:
            self.liquidation_details.text = f"Error al calcular la liquidación: {str(e)}"
    
    def go_back(self, *args):
        self.manager.current = 'data'
    
    def go_to_compensation(self, *args):
        self.manager.current = 'compensation'

# Screen for calculating compensation
class CompensationScreen(Screen):
    def __init__(self, **kwargs):
        super(CompensationScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.compensation_label = Label(text="Cálculo de la Indemnización", font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(self.compensation_label)

        # Add the type of contract
        contract_type_label = Label(text="Tipo de contrato", font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(contract_type_label)

        self.contract_type_spinner = Spinner(text="Seleccione el tipo de contrato", values=("fijo_1_año", "fijo_inferior_1_año", "indefinido"))
        self.layout.add_widget(self.contract_type_spinner)

        start_date_label = Label(text="Fecha de inicio del contrato", font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(start_date_label)

        self.start_date_input = TextInput(multiline=False, font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(self.start_date_input)

        end_date_label = Label(text="Fecha de Fin del contrato:", font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(end_date_label)

        self.end_date_input = TextInput(multiline=False, font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(self.end_date_input)

        calculate_button = Button(text="Calcular Indemnización", font_size=FONT_SIZE, font_name=FONT_NAME)
        calculate_button.bind(on_release=self.calculate_compensation_button)
        self.layout.add_widget(calculate_button)
        #      
    
        self.compensation_details = Label(text="", font_size=FONT_SIZE, font_name=FONT_NAME)
        self.layout.add_widget(self.compensation_details)
        
        back_button = Button(text="Volver", font_size=FONT_SIZE, font_name=FONT_NAME)
        back_button.bind(on_release=self.go_back)
        self.layout.add_widget(back_button)
        
        self.add_widget(self.layout)
    
    def on_enter(self, *args):
        self.calculate_compensation_button()

    def calculate_compensation_button(self, *args):            
        try:
            type_of_contract = self.contract_type_spinner.text
            start_date = self.start_date_input.text
            end_date = self.end_date_input.text

            employee = self.manager.employee

            # Calculate compensation
            compensation = calculate_compensation(employee, type_of_contract, start_date, end_date)

            # Showing results
            results = f"Indemnización Total: {compensation}"
            self.compensation_details.text = results

        except EmployeeException as e:
            self.compensation_details.text = f"Error al calcular la indemnización: {str(e)}"
    
    def go_back(self, *args):
        self.manager.current = 'result'

# Pantalla principal para manejar la navegación
class LiquidationApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(EmployeeDataScreen(name='data'))
        sm.add_widget(ResultScreen(name='result'))
        sm.add_widget(CompensationScreen(name='compensation'))
        return sm

if __name__ == "__main__":
    LiquidationApp().run()
