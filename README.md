Aquí tienes el README actualizado con las instrucciones para ejecutar los casos de prueba del archivo `Testsdb.py` y también para ejecutar el archivo `consoledb.py`:

---

# **Proyecto de Liquidación de Empleados del Sector Privado**

## **Quien hizo esto?**

Los integrantes y colaboradores del proyecto son:

- John Steven Ceballos Agudelo
- Gustavo Mendez 

## **Qué es y para qué es?**

Es un proyecto de liquidación de nómina para un empleado del sector privado. Se encarga de realizar la liquidación de un empleado cuando ha finalizado su contrato laboral.

## **Cómo hacerlo funcionar?**

- Antes de poder ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

1. **Instalar Python**: Descargar e instalar Python desde [python.org](http://python.org). Asegúrate de marcar la opción "Add Python to PATH" para facilitar la ejecución de comandos de Python desde la terminal.

2. **Instalar Git**: Descargar e instalar Git desde [git-scm.com](http://git-scm.com).

3. **Instalar pandas**: 

   ```bash
    pip install pandas 
   ```



### **Pasos para ejecutar el proyecto desde la consola de Windows:**

1. Abrir la Consola de Windows y navegar al directorio donde deseas clonar el repositorio:
   ```bash
   cd C:\Users\TuUsuario\Proyectos
   ```

2. Clonar el Repositorio: Usar el comando **git clone** seguido de la URL del repositorio:
   ```bash
   git clone https://github.com/JHONCE79/Liquidation-proyect.git
   ```

3. Navegar al Directorio del Proyecto: Después de clonar el repositorio, ir al directorio del proyecto:
   ```bash
   cd Liquidation-proyect
   ```

4. Ejecutar el proyecto: Navegar al directorio principal del proyecto:
   ```bash
   src\Console\LiquidationConsole.py
   ```

---

## **Ejecución de la Interfaz Gráfica**

Para ejecutar la interfaz gráfica del proyecto se debe realizar lo siguiente:

1. **Abrir la consola de Windows**: Presiona `Windows + R`, escribe `cmd` y presiona `Enter`. Esto abrirá la consola de comandos.

2. **Instalar Kivy**: Asegúrate de tener instalada la librería de Kivy. Ejecuta el siguiente comando para instalar Kivy:
   ```bash
   pip install kivy
   ```

3. **Ubicarse en la carpeta del proyecto**: Navegar al directorio donde se encuentra la interfaz:
   ```bash
   cd src\GUI\
   ```

4. **Ejecutar la interfaz gráfica**: Ejecuta el archivo que lanza la interfaz gráfica:
   ```bash
   python Liquidation_gui.py
   ```

---

## **Ejecución de los Casos de Prueba**

Para asegurar que todo el código funciona correctamente, se han creado pruebas unitarias en el archivo `Testsdb.py`. A continuación te explico cómo ejecutarlas:

1. **Instalar dependencias**: Asegúrate de tener instaladas todas las bibliotecas necesarias, en particular `unittest`. Este paquete ya viene incluido en Python, por lo que no es necesario instalarlo.

2. **Ubicarse en el directorio de pruebas**: Navegar al directorio donde están los archivos de prueba:
   ```bash
   cd tests\
   ```

3. **Ejecutar las pruebas unitarias**: Ejecuta el archivo `Testsdb.py` con el siguiente comando:
   ```bash
   python -m unittest Testsdb.py
   ```

Esto ejecutará todas las pruebas unitarias y mostrará los resultados de cada una.

---

## **Ejecución del archivo de consola de la base de datos "consoledb.py"**

El archivo `consoledb.py` es otro componente del proyecto que se puede ejecutar directamente desde la consola. Para hacerlo, sigue estos pasos:

1. **Navegar al directorio donde se encuentra el archivo**:
   ```bash
   cd src\View\
   ```

2. **Ejecutar el archivo**:
   ```bash
   python consoledb.py
   ```

Esto lanzará la versión en consola del sistema de liquidación de empleados.

---

## **Cómo está hecho?**

Para la realización de este proyecto se hizo uso de varias librerías, como:

- **datetime**: Para configurar el formato de las fechas de manera correcta.
- **unittest**: Permite crear y ejecutar pruebas para asegurarse de que el código funcione correctamente.
- **sys**: Proporciona acceso a las variables y funciones relacionadas con el sistema.

El proyecto está organizado en tres carpetas principales, cada una con un propósito específico:

1. **.vscode**:
Esta carpeta almacena configuraciones específicas del editor Visual Studio Code. Dentro de ella se encuentra el archivo ```settings.json```, que configura el entorno para usar la librería ```unittest```, la cual ejecuta las pruebas unitarias del proyecto.

2. **src**:
Esta carpeta contiene un archivo ```__init__.py``` que permite que Python reconozca la carpeta como un módulo, facilitando la importación de sus componentes. Además, incluye tres subcarpetas:

- *Console*: Contiene dos archivos: ```__init__.py```, que permite el reconocimiento de la carpeta como un módulo, y LiquidationConsole.py, que implementa la interfaz con el usuario.

- *Logic*: Esta carpeta alberga tres archivos:

1. ```__init__.py```: que permite el reconocimiento de la carpeta como un módulo.

2. ```employee.py```: que define las variables necesarias para la lógica del programa.

3. ```Liquidation.py```: que contiene la lógica completa del proceso de liquidación, importando las variables desde ```employee.py```.También incluye una subcarpeta ```__pycache__```, una optimización automática de Python para acelerar la ejecución del código.

- *GUI*: Esta carpeta alberga cuatro archivos esenciales para la interfaz gráfica del proyecto:

1. ```__init__.py```: Este archivo vacío permite que Python reconozca la carpeta como un módulo, facilitando la importación de sus contenidos.

2. ```FUNNY SUNSHINE.ttf```: Un archivo de fuente que proporciona un estilo visual específico para elementos de la interfaz gráfica

3. ``` Liquidation_gui.py```: Contiene toda la lógica y estructura de la interfaz gráfica de usuario, siendo el componente principal para la presentación visual del programa

4. ``` Londona-regular.otf```: Otro archivo de fuente que ofrece un estilo alternativo para los textos en la interfaz, permitiendo una mayor variedad en el diseño visual


3. **tests**:

Esta carpeta está dedicada a las pruebas unitarias del proyecto. Contiene dos archivos:

1. ```__init__.py```, que permite que la carpeta sea reconocida como un módulo.

2. ```LiquidationTests.py```, que agrupa todas las pruebas unitarias del proyecto. También incluye una subcarpeta ```__pycache__```, similar a la encontrada en ```Logic```, para optimizar la ejecución del código.


En la carpeta principal del proyecto, **Liquidation-proyect**, se encuentran los siguientes archivos:

- ```__init__.py```: Permite que toda la carpeta principal sea reconocida como un módulo.

- ```.gitignore```: Contiene las rutas y archivos que se excluyen del control de versiones con Git.

- ```LICENSE```: Especifica los términos y condiciones bajo los cuales se puede utilizar, modificar y distribuir el código fuente del proyecto.

- ```README.md```: Proporciona la documentación y explicación necesarias para entender y trabajar con el proyecto.
