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

4. Ejecutar el proyecto: Navegar al directiorio principal del proyecto
``` src\Console\LiquidationConsole.py```

## **Ejecución de la interfaz gráfica**

Para ejecutar la interfaz gráfica del proyecto se debe de realizar lo siguiente:

1. Abrir la consola de windows: Presiona ```Windows + R```, escribe cmd y presiona ```Enter```. Esto abrirá la consola de comandos

2. Instalar kivy: Asegurarse de tener instalada la librería de kivy en el entorno. Luego, ejecuta el siguiente comando para instalar kivy ```pip install kivy```

3. Ubicarse en la carpeta dentro del proyecto:

## **Como está hecho?**

Para la realización de este proyecto se hizo uso de varias librerias, como:

- **datetime:** Para configurar el formato de las fechas de manera correcta
- **unittest:** Esta biblioteca permite crear y ejecutar pruebas para asegurarse de que el código funcione correctamente
- **sys:** Proporciona acceso a las variables y funciones relacionadas con el sistema

El proyecto está organizado en tres carpetas principales, cada una con un propósito específico:

1. **.vscode**:
Esta carpeta almacena configuraciones específicas del editor Visual Studio Code. Dentro de ella se encuentra el archivo ```settings.json```, que configura el entorno para usar la librería ```unittest```, la cual ejecuta las pruebas unitarias del proyecto.

2. **src**:
Esta carpeta contiene un archivo ```__init__.py``` que permite que Python reconozca la carpeta como un módulo, facilitando la importación de sus componentes. Además, incluye dos subcarpetas:

- *Console*: Contiene dos archivos: ```__init__.py```, que permite el reconocimiento de la carpeta como un módulo, y LiquidationConsole.py, que implementa la interfaz con el usuario.

- *Logic*: Esta carpeta alberga tres archivos:

1. ```__init__.py```, que permite el reconocimiento de la carpeta como un módulo.

2. ```employee.py```, que define las variables necesarias para la lógica del programa.

3. ```Liquidation.py```, que contiene la lógica completa del proceso de liquidación, importando las variables desde ```employee.py```.También incluye una subcarpeta ```__pycache__```, una optimización automática de Python para acelerar la ejecución del código.


3. **tests**:

Esta carpeta está dedicada a las pruebas unitarias del proyecto. Contiene dos archivos:

1. ```__init__.py```, que permite que la carpeta sea reconocida como un módulo.

2. ```LiquidationTests.py```, que agrupa todas las pruebas unitarias del proyecto. También incluye una subcarpeta ```__pycache__```, similar a la encontrada en ```Logic```, para optimizar la ejecución del código.


En la carpeta principal del proyecto, **Liquidation-proyect**, se encuentran los siguientes archivos:

- ```__init__.py```: Permite que toda la carpeta principal sea reconocida como un módulo.

- ```.gitignore```: Contiene las rutas y archivos que se excluyen del control de versiones con Git.

- ```LICENSE```: Especifica los términos y condiciones bajo los cuales se puede utilizar, modificar y distribuir el código fuente del proyecto.

- ```README.md```: Proporciona la documentación y explicación necesarias para entender y trabajar con el proyecto.
