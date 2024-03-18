# Pasos para inciar el servidor

## Liberias
* tener instalado Python y Django
* Para instalar Djando ejecutar el comando: pip install django

## Ejecutar el servidor
    ```
    Python manage.py runserver
    ```

## Ejecutar en caso de hacer cambios en el modelo de base de datos
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

## Acceder al panel de administración
* http://127.0.0.1:8000/admin
* usuario: admin
* contraseña: admin