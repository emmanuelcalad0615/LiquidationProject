Aquí tienes el README actualizado con las instrucciones para ejecutar los casos de prueba del archivo `Testsdb.py` y también para ejecutar el archivo `consoledb.py`:

---

# **Proyecto de Liquidación de Empleados del Sector Privado**

## **Quien hizo esto?**

Los integrantes y colaboradores del proyecto son:

- John Steven Ceballos Agudelo

## **Qué es y para qué es?**

Es un proyecto de liquidación de nómina para un empleado del sector privado. Se encarga de realizar la liquidación de un empleado cuando ha finalizado su contrato laboral.

## **Cómo hacerlo funcionar?**

- Antes de poder ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

1. **Instalar Python**: Descargar e instalar Python desde [python.org](http://python.org). Asegúrate de marcar la opción "Add Python to PATH" para facilitar la ejecución de comandos de Python desde la terminal.

2. **Instalar Git**: Descargar e instalar Git desde [git-scm.com](http://git-scm.com).

### **Pasos para ejecutar el proyecto desde la consola de Windows:**

1. Abrir la Consola de Windows y navegar al directorio donde deseas clonar el repositorio:
   ```bash
   cd C:\Users\TuUsuario\Proyectos
   ```

2. Clonar el Repositorio: Usar el comando **git clone** seguido de la URL del repositorio:
   ```bash
   git clone https://github.com/usuario/nombre-del-repositorio.git
   ```

3. Navegar al Directorio del Proyecto: Después de clonar el repositorio, ir al directorio del proyecto:
   ```bash
   cd nombre-del-repositorio
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
   cd src\tests
   ```

3. **Ejecutar las pruebas unitarias**: Ejecuta el archivo `Testsdb.py` con el siguiente comando:
   ```bash
   python -m unittest Testsdb.py
   ```

Esto ejecutará todas las pruebas unitarias y mostrará los resultados de cada una.

---

## **Ejecución del archivo consoledb.py**

El archivo `consoledb.py` es otro componente del proyecto que se puede ejecutar directamente desde la consola. Para hacerlo, sigue estos pasos:

1. **Navegar al directorio donde se encuentra el archivo**:
   ```bash
   cd src\Console\
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

El proyecto está organizado en tres carpetas principales, cada una con un propósito específico...

(El resto del README permanece igual.)

--- 

