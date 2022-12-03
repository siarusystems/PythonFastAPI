# PythonFastAPI

Qué hace el proyecto?

Api en python usando FastAPI micro framework.

Realiza 3 CRUD a entidades:
* Entidad Vacante (Create, Read, Update, Delete, GetById)
* Entidad Usuario (Create, Read, Update, Delete, GetById)
* Entidad Empresa (Create, Read, Update, Delete, GetById)
* EndPoint adicional BuscarOfertasLaborales el cual retorna ofertas laborales de acuerdo a tiempo de experiencia y skill requeridos por la vacante

Usa mySql como Base de Datos
Usa Libreria Python Mysql.Connector
Usa Libreria pydantic para mapear modelos
Aquitectura distribuida en capa sencilla y minimalista: main.py --> models --> configBD --> test


Cómo pueden comenzar los usuarios con el proyecto?

correr por consola uvicorn (server asyncrono para python), navegar hasta raiz del proyecto y ejecutar: uvicorn main:app --reload

primera visita sugerida desps de correr el proyecto: localhost:8000/docs

FastAPI Genera auto magicamente docuementacion OpenApi de swager en la ruta: localhost:8000/docs

Nota 1: Puerto puede ser cambiado por defecto pasandolo como parametro al iniciar uvicorn ;)

Nota 2: Como mejora a futuro se podria empaquetar en una imagen docker y realizar mas validaciones internas de acuerdo a una logica de negocio establecidad.

Nota 3: Recomiendo IDE PyCharm para trabajar con Python...
