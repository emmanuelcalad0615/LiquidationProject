Proyecto de Liquidación de Empleados del Sector Privado
¿Quién hizo esto?
Los integrantes y colaboradores del proyecto son:
•	Emmanuel Calad
•	Sofia Correa Carmona
¿Qué es y para qué es?
Es un proyecto de liquidación de nómina para un empleado del sector privado. Se encarga de realizar la liquidación de un empleado cuando ha finalizado su contrato laboral.
¿Cómo hacerlo funcionar?
Antes de poder ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:
1.	Instalar Python: Descargar e instalar Python desde python.org. Asegúrate de marcar la opción "Add Python to PATH" para facilitar la ejecución de comandos de Python desde la terminal.
2.	Instalar Git: Descargar e instalar Git desde git-scm.com.
3.	Instalar pandas: Ejecuta el siguiente comando en la terminal:
pip install pandas


Crear un entorno virtual
Antes de instalar los paquetes necesarios, se recomienda crear un entorno virtual. Ejecute los siguientes comandos:
Windows:
py -m venv .venv
.venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate
Requisitos de instalación
Una vez activado el entorno virtual, instale los paquetes necesarios mediante el archivo requirements.txt:
pip install -r requirements.txt


Ejecutar el programa
Ejecución de la consola:
Ejecute el archivo console.py:
py src\Console\console.py



Paso a paso desde la terminal para ejecutar la interfaz web:

1.	Clonar el Repositorio: Usar el comando git clone seguido de la URL del repositorio:
git clone https://github.com/emmanuelcalad0615/LiquidationProject.git
Ahora habrás clonado el repositorio en tu máquina local y podrás comenzar a trabajar con él.________________________________________
Ejecutar el Archivo app.py:
Ahora estás en la ubicación donde se encuentra el archivo app.py. Para ejecutarlo, utiliza el siguiente comando:
python app.py
•	Presiona Enter para ejecutar el comando. Aparecerá un mensaje similar a este:
•	* Running on http://127.0.0.1:5000
•	Press CTRL+C to quit   
•	 * Restarting with stat
•	 * Debugger is active!
•	 * Debugger PIN: 142-577-729
•	Copia el enlace de "Running on" (en este caso, http://127.0.0.1:5000) y pégalo en tu navegador, o presiona ctrl y haz clic en el enlace para seguirlo directamente. Ahora podrás acceder a tu aplicación web en el navegador utilizando la dirección proporcionada. Gracias por la corrección. Aquí está la guía actualizada:
Cómo ejecutar los test

Para ejecutar los casos de prueba deberá de escribir en la terminal de python los siguientes comandos:
Este ejecutará los casos de prueba para la calculadora de hipoteca inversa: 
python tests/ LiquidationTests.py
Este ejecutará los casos de prueba para la base de datos: 
python tests/ Testsdb.py

Ejecución de la Interfaz Gráfica
Para ejecutar la interfaz gráfica del proyecto, sigue estos pasos:
1.	Abrir la consola de Windows: Presiona Windows + R, escribe cmd y presiona Enter.
2.	Instalar Kivy: Asegúrate de tener instalada la librería de Kivy. Ejecuta el siguiente comando para instalar Kivy:
pip install kivy
3.	Ubicarse en la carpeta del proyecto: Navegar al directorio donde se encuentra la interfaz:
cd src\GUI\
4.	Ejecutar la interfaz gráfica: Ejecuta el archivo que lanza la interfaz gráfica:
python Liquidation_gui.py
________________________________________
________________________________________
Ejecución del archivo de consola de la base de datos "consoledb.py"
El archivo consoledb.py es otro componente del proyecto que se puede ejecutar directamente desde la consola. Para hacerlo, sigue estos pasos:
1.	Navegar al directorio donde se encuentra el archivo:
cd src\View\
2.	Ejecutar el archivo:
python consoledb.py
Esto lanzará la versión en consola del sistema de liquidación de empleados.
________________________________________
¿Cómo está hecho?
Para la realización de este proyecto se hizo uso de varias librerías, como:
•	datetime: Para configurar el formato de las fechas de manera correcta.
•	unittest: Permite crear y ejecutar pruebas para asegurarse de que el código funcione correctamente.
•	sys: Proporciona acceso a las variables y funciones relacionadas con el sistema.
El proyecto está organizado en tres carpetas principales, cada una con un propósito específico:
1.	.vscode:
Esta carpeta almacena configuraciones específicas del editor Visual Studio Code. Dentro de ella se encuentra el archivo settings.json, que configura el entorno para usar la librería unittest, la cual ejecuta las pruebas unitarias del proyecto.
2.	src:
Esta carpeta contiene un archivo __init__.py que permite que Python reconozca la carpeta como un módulo, facilitando la importación de sus componentes. Además, incluye tres subcarpetas:
o	Console: Contiene dos archivos: __init__.py, que permite el reconocimiento de la carpeta como un módulo, y LiquidationConsole.py, que implementa la interfaz con el usuario.
o	Logic: Alberga tres archivos:
	__init__.py: permite el reconocimiento de la carpeta como un módulo.
	employee.py: define las variables necesarias para la lógica del programa.
	Liquidation.py: contiene la lógica completa del proceso de liquidación, importando las variables desde employee.py. Incluye una subcarpeta __pycache__, que optimiza la ejecución del código.
o	GUI: Contiene cuatro archivos esenciales para la interfaz gráfica del proyecto:
	__init__.py: permite que Python reconozca la carpeta como un módulo.
	FUNNY SUNSHINE.ttf: archivo de fuente que proporciona un estilo visual específico para elementos de la interfaz gráfica.
	Liquidation_gui.py: contiene toda la lógica y estructura de la interfaz gráfica de usuario.
	Londona-regular.otf: otro archivo de fuente que ofrece un estilo alternativo para los textos en la interfaz.
3.	tests:
Dedicada a las pruebas unitarias del proyecto. Contiene dos archivos:
o	__init__.py, que permite que la carpeta sea reconocida como un módulo.
o	LiquidationTests.py, que agrupa todas las pruebas unitarias del proyecto. También incluye una subcarpeta __pycache__, similar a la encontrada en Logic, para optimizar la ejecución del código.
En la carpeta principal del proyecto, Liquidation-proyect, se encuentran los siguientes archivos:
•	__init__.py: permite que toda la carpeta principal sea reconocida como un módulo.
•	.gitignore: contiene las rutas y archivos que se excluyen del control de versiones con Git.
•	LICENSE: especifica los términos y condiciones bajo los cuales se puede utilizar, modificar y distribuir el código fuente del proyecto.
•	README.md: proporciona la documentación y explicación necesarias para entender y trabajar con el proyecto.
