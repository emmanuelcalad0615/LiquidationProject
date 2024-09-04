# **Proyecto de Liquidación de Empleados del Sector Privado**

## **Quien hizo esto?**

Los integrantes y colaboradores del proyecto son:

- Samuel Gallego Meneses
- Juliana Franco Alzate
- Sara Moncada Correa

## **Que es y para que es?**

Es un proyecto de liquidación de nómina para un empleado del sector privado. Se encarga de realizar la liquidación de un empleado cuando ha finalizado su contrato laboral.

## **Cómo lo hago funcionar?**

- Antes de poder ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

1. Instalar Python: Descargar e instalar Python desde http://python.org. Marcar la opción "Add Python to PATH" para facilitar la ejecución de comandos de Python desde la terminal.

2. Instalar Git: Descargar e instalar Git desde http://git-scm.com.

- Pasos para ejecutar el proyecto desde la consola de windows:

1. Abrir la Consola de Windows y navegar al directorio donde deseas clonar el repositorio.
```cd C:\Users\TuUsuario\Proyectos```

2. Clonar el Repositorio: Usar el comando **git clone** seguido de la URL del repositorio.
```git clone https://github.com/usuario/nombre-del-repositorio.git```

3. Navegar al Directorio del Proyecto: Después de clonar el repositorio, ir al directorio del proyecto.
```cd nombre-del-repositorio```

4. Crear y Activar un Entorno Virtual:

- Crear un entorno virtual: ```python -m venv venv```

- Activar el entorno virtual, en el símbolo del sistema:
```.\venv\Scripts\activate```

- Activar el entorno, en el powershell de windows: ```.\venv\Scripts\Activate.ps1.```

5. Instalar Dependencias del Proyecto: ```pip install -r requirements.txt```

6. Ejecutar el proyecto: ```python main.py```.
Reemplazar el nombre ```main.py``` por el nombre del archivo principal del proyecto.

## **Como está hecho?**

Para la realización de este proyecto se hizo uso de varias librerias, como:

- **datetime:** Para configurar el formato de las fechas de manera correcta
- **unittest:** Esta biblioteca permite crear y ejecutar pruebas para asegurarse de que el código funcione correctamente
- **sys:** Proporciona acceso a las variables y funciones relacionadas con el sistema