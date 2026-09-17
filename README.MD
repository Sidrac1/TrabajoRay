# Instalación del programa:
1. Clonar el repositorio
~~~
git clone https://github.com/Sidrac1/TrabajoRay.git
~~~

2. Crear el entorno virtual:

### en Windows 
~~~
# Creación del entorno virtual:
python -m venv .venv

# Activación del entorno virtual en PowerShell:
.\.venv\Scripts\Activate.ps1

# En CMD
.venv\Scripts\activate.bat

~~~
### en linux
~~~
# Creación del entorno virtual:
python3 -m venv mi_entorno

# Activación del entorno virtual
source .venv/bin/activate

~~~

## Instala las librerías
~~~
pip install -r requirements.txt
~~~

## Corre el programa
~~~
# En Windows
python manage.py runserver
# En Linux
python3 manage.py runserver
~~~

# Consideraciones tras la instalación:
1. Aunque el sistema ya funciona es necesario que hagas modificaciones en el archivo "settings.py" de acuerdo al motor de BD que utilices y tus credenciales

2. Es necesario aún hacer las migraciones. puedes usar el siguiente comando:
~~~
# En Windows
python3 manage.py makemigrations
python3 manage.py migrate

# En Linux
python3 manage.py makemigrations
python3 manage.py migrate
~~~


# Por favor ayuda a colaborar con este repo para que todos tengamos la chamba al corriente