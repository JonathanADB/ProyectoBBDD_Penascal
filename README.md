# ProyectoBBDD_Penascal

## pasos que hemos usado para la crecion del proyecto

### Creación de la estructura del proyecto
1. mkdir app app/routers app/templates
touch app/__init__.py app/main.py app/models.py app/schemas.py app/crud.py app/dependencies.py app/routers/__init__.py app/routers/courses.py app/routers/admin.py
touch requirements.txt

### Creación de un entorno virtual
2.python -m venv env
  source env/bin/activate

### Dependecncias que usaremos archivo requirements.txt
fastapi
uvicorn
sqlalchemy
mysql-connector-python
jinja2
3. pip install -r requirements.txt

### Arrancar servidor
4.uvicorn app.main:app --reload



