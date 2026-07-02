# Taller Express

Aplicación web para la gestión de productos de un taller mecánico, desarrollada con Django.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/urfavsebxs/Repositorio-Actividad2.git
cd Repositorio-Actividad2
```

2. Crear un entorno virtual e instalar dependencias:
```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install django
```

3. Aplicar migraciones:
```bash
python manage.py migrate
```

4. Crear un superusuario (opcional):
```bash
python manage.py createsuperuser
```

5. Ejecutar el servidor:
```bash
python manage.py runserver
```

6. Abrir en el navegador: `http://127.0.0.1:8000/`
