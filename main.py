from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from models.models import Vacante, Usuario, Empresa
from configDB.DB import cnx
#import time,sys


app = FastAPI(title='Prueba Juan Diego Mora Echeverri - Backend Python',description='Esta es una API con FastApi en Python',version='1.0.1')



#inicio de operaciones CRUD clase Vacante
#inicio de operaciones CRUD clase Vacante

@app.post("/Vacante/")
async def insertVacante(vacante: Vacante):
    cursor1 = cnx.cursor()
    add_vacante = ("INSERT INTO vacante (PositionName, CompanyName, Salary, Currency, VacancyId, VacancyLink, RequiredSkills, YearsPreviousExperience,  InternalCode) "
    		"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_employee3 = (vacante.PositionName, vacante.CompanyName, vacante.Salary, vacante.Currency, vacante.VacancyId, vacante.VacancyLink, vacante.RequiredSkills, vacante.YearsPreviousExperience, vacante.InternalCode)
    cursor1.execute(add_vacante, data_employee3)
    emp_no = cursor1.lastrowid
    cnx.commit()
    return {"ultimoId": emp_no}
    


@app.delete("/Vacante/{vacante_id}")
async def read_item(vacante_id: int):
    cursor2 = cnx.cursor()
    delete_vacante = "DELETE FROM vacante WHERE Id='%s'"
    cursor2.execute(delete_vacante % vacante_id)
    cnx.commit()
    return {"Id_Registro_Solicitado_A_Borrar": vacante_id}



@app.put("/Vacante/")
async def update_item(vacante: Vacante):
    cursor2 = cnx.cursor()
    update_vacante = "UPDATE vacante set PositionName=%s, CompanyName=%s, Salary=%s, Currency=%s, VacancyId=%s, VacancyLink=%s, RequiredSkills=%s, YearsPreviousExperience=%s WHERE InternalCode=%s"
    cursor2.execute(update_vacante, (vacante.PositionName, vacante.CompanyName, vacante.Salary, vacante.Currency, vacante.VacancyId, vacante.VacancyLink, vacante.RequiredSkills, vacante.YearsPreviousExperience, vacante.InternalCode))
    cnx.commit()
    return {"Internal_Cdoe_Solicitado_A_Update": vacante.InternalCode}
    


@app.get("/Vacante/")
async def get_all_items():
    cursor3 = cnx.cursor()
    get_vacante = "SELECT * FROM vacante"
    cursor3.execute(get_vacante)
    data = cursor3.fetchall()
    cnx.commit()
    return data
    

@app.get("/Vacante/{vacante_id}")
async def get_all_items_by_id(vacante_id: int):
    cursor3 = cnx.cursor()
    get_vacante = "SELECT * FROM vacante WHERE Id='%s'"
    cursor3.execute(get_vacante % vacante_id)
    data = cursor3.fetchall()
    cnx.commit()
    return data
    
#fin de operaciones CRUD clase Vacante
#fin de operaciones CRUD clase Vacante



#inicio de operaciones CRUD clase Usuario
#inicio de operaciones CRUD clase Usuario

@app.post("/Usuario/")
async def insertUsuario(usuario: Usuario):
    cursor1 = cnx.cursor()
    add_usuario = ("INSERT INTO usuario (UserId, FirstName, LastName, Email, YearsPreviousExperience, Skills, InternalCode) "
    		"VALUES (%s, %s, %s, %s, %s, %s, %s)")
    data_usuario = (usuario.UserId, usuario.FirstName, usuario.LastName, usuario.Email, usuario.YearsPreviousExperience, usuario.Skills, usuario.InternalCode)
    cursor1.execute(add_usuario, data_usuario)
    emp_no = cursor1.lastrowid
    cnx.commit()
    return {"ultimoId": emp_no}
    


@app.delete("/Usuario/{usuario_id}")
async def read_item2(usuario_id: int):
    cursor2 = cnx.cursor()
    delete_usuario = "DELETE FROM usuario WHERE Id='%s'"
    cursor2.execute(delete_usuario % usuario_id)
    cnx.commit()
    return {"Id_Registro_Solicitado_A_Borrar": usuario_id}



@app.put("/Usuario/")
async def update_item2(usuario: Usuario):
    cursor2 = cnx.cursor()
    update_usuario = "UPDATE usuario SET UserId=%s, FirstName=%s, LastName=%s, Email=%s, YearsPreviousExperience=%s, Skills=%s WHERE InternalCode=%s"
    cursor2.execute(update_usuario, (usuario.UserId, usuario.FirstName, usuario.LastName, usuario.Email, usuario.YearsPreviousExperience, usuario.Skills, usuario.InternalCode))
    cnx.commit()
    return {"Internal_Cdoe_Solicitado_A_Update": usuario.InternalCode}
    


@app.get("/Usuario/")
async def get_all_items2():
    cursor3 = cnx.cursor()
    get_usuario = "SELECT * FROM usuario"
    cursor3.execute(get_usuario)
    data = cursor3.fetchall()
    cnx.commit()
    return data
    

@app.get("/Usuario/{usuario_id}")
async def get_all_items_by_id2(usuario_id: int):
    cursor3 = cnx.cursor()
    get_usuario = "SELECT * FROM usuario WHERE Id='%s'"
    cursor3.execute(get_usuario % usuario_id)
    data = cursor3.fetchall()
    cnx.commit()
    return data
    
#fin de operaciones CRUD clase Usuario
#fin de operaciones CRUD clase Usuario


    

#inicio de operaciones CRUD clase Empresa
#inicio de operaciones CRUD clase Empresa

@app.post("/Empresa/")
async def insertEmpresa(empresa: Empresa):
    cursor1 = cnx.cursor()
    add_empresa = ("INSERT INTO empresa (Name, City, InternalCode) "
    		"VALUES (%s, %s, %s)")
    data_empresa = (empresa.Name, empresa.City, empresa.InternalCode)
    cursor1.execute(add_empresa, data_empresa)
    emp_no = cursor1.lastrowid
    cnx.commit()
    return {"ultimoId": emp_no}
    


@app.delete("/Empresa/{empresa_id}")
async def read_item3(empresa_id: int):
    cursor2 = cnx.cursor()
    delete_empresa = "DELETE FROM empresa WHERE Id='%s'"
    cursor2.execute(delete_empresa % empresa_id)
    cnx.commit()
    return {"Id_Registro_Solicitado_A_Borrar": empresa_id}



@app.put("/Empresa/")
async def update_item3(empresa: Empresa):
    cursor2 = cnx.cursor()
    update_empresa = "UPDATE empresa SET Name=%s, City=%s WHERE InternalCode=%s"
    cursor2.execute(update_empresa, (empresa.Name, empresa.City, empresa.InternalCode))
    cnx.commit()
    return {"Internal_Cdoe_Solicitado_A_Update": empresa.InternalCode}
    


@app.get("/Empresa/")
async def get_all_items3():
    cursor3 = cnx.cursor()
    get_empresa = "SELECT * FROM empresa"
    cursor3.execute(get_empresa)
    data = cursor3.fetchall()
    cnx.commit()
    return data
    

@app.get("/Empresa/{empresa_id}")
async def get_all_items_by_id3(empresa_id: int):
    cursor3 = cnx.cursor()
    get_empresa = "SELECT * FROM empresa WHERE Id='%s'"
    cursor3.execute(get_empresa % empresa_id)
    data = cursor3.fetchall()
    cnx.commit()
    return data
    
#fin de operaciones CRUD clase Empresa
#fin de operaciones CRUD clase Empresa




@app.post("/BuscarOfertasLaborales/")
async def buscar_ofertas(usuario: Usuario):
    cursor4 = cnx.cursor()
    get_vacantes = "SELECT * FROM vacante WHERE RequiredSkills = %s OR YearsPreviousExperience = %s"
    cursor4.execute(get_vacantes, (usuario.Skills, usuario.YearsPreviousExperience))
    data = cursor4.fetchall()
    cnx.commit()
    return data


    
@app.get("/Bienvenida",  response_class=HTMLResponse)
def show_html():
    return generate_html_response()
    
    
    
@app.get("/")
async def read_root():
    return {"Hello": "World"}


    
#inicio de funciones de ayuda
#inicio de funciones de ayuda
    
def generate_html_response() -> HTMLResponse:
    html_content = """
    <html>
        <head>
            <title>Prueba juan diego mora</title>
            <script>function funcionJuan(){
	alert('no disponible en el momento !! \\n\\nDisculpa las molestias !! Vuelve pronto')
	}</script>
        </head>
        <body><center><h1>Prueba Juan Diego Mora Echeverri</h1></center><br><br>
            <a href='/docs' target='_blank'>Abrir docs openApi - Swager</a>
        <br><br><br><br>
            <a onclick='funcionJuan()' target='_blank'>abrir Utilidaes</a>
        <br><br><br><br>
	
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
    
    
#fin de funciones de ayuda
#fin de funciones de ayuda





    
    
