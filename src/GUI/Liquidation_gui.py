from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import os
import sys
sys.path.append("src")
# Importando los módulos requeridos
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

# Pantalla de Bienvenida
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        welcome_label = Label(text="Bienvenido al Programa de Liquidación", font_size='24sp')
        start_button = Button(text="Iniciar", size_hint=(1, 0.2))
        start_button.bind(on_release=self.go_to_data)
        
        layout.add_widget(welcome_label)
        layout.add_widget(start_button)
        self.add_widget(layout)

    def go_to_data(self, *args):
        self.manager.current = 'data'

# Pantalla para ingresar los datos del empleado
class EmployeeDataScreen(Screen):
    def __init__(self, **kwargs):
        super(EmployeeDataScreen, self).__init__(**kwargs)
        self.layout = GridLayout(cols=2, padding=10, spacing=10)
        
        self.layout.add_widget(Label(text="Salario Básico Mensual:"))
        self.salary_input = TextInput(multiline=False)
        self.layout.add_widget(self.salary_input)
        
        self.layout.add_widget(Label(text="Auxilio de Transporte:"))
        self.transport_input = TextInput(multiline=False)
        self.layout.add_widget(self.transport_input)
        
        self.layout.add_widget(Label(text="Días Trabajados:"))
        self.days_input = TextInput(multiline=False)
        self.layout.add_widget(self.days_input)
        
        submit_button = Button(text="Calcular Liquidación")
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
            
            # Verificar excepciones
            verify_exceptions(employee)
            
            # Guardar el empleado en la instancia del administrador de pantallas
            self.manager.employee = employee
            self.manager.current = 'result'
            
        except (NegativeValueError, IncorrectDataTypeError, DivisionByZeroError, NumberOutOfRangeError) as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error al crear el objeto empleado: {str(e)}")

# Pantalla para mostrar los resultados de la liquidación
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.result_label = Label(text="Resultados de la Liquidación", font_size='18sp')
        self.layout.add_widget(self.result_label)
        
        self.liquidation_details = Label(text="")
        self.layout.add_widget(self.liquidation_details)
        
        back_button = Button(text="Volver", size_hint=(1, 0.2))
        back_button.bind(on_release=self.go_back)
        self.layout.add_widget(back_button)
        
        self.add_widget(self.layout)
    
    def on_enter(self, *args):
        employee = self.manager.employee
        
        try:
            # Calcular los diferentes componentes de la liquidación
            severance_pay = calculate_severance_pay_amount(employee)
            severance_pay_interest = calculate_severance_pay_interest(employee, severance_pay)
            service_bonus = calculate_service_bonus(employee)
            vacation = calculate_vacation(employee)
            
            total_liquidation = severance_pay + severance_pay_interest + service_bonus + vacation

            # Mostrar resultados
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

# Pantalla principal para manejar la navegación
class LiquidationApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(EmployeeDataScreen(name='data'))
        sm.add_widget(ResultScreen(name='result'))
        return sm

if __name__ == "__main__":
    LiquidationApp().run()
