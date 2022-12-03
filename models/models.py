from pydantic import BaseModel


class Vacante(BaseModel):
    PositionName: str
    CompanyName: str
    Salary: int
    Currency: str
    VacancyId: int
    VacancyLink: str
    RequiredSkills: str
    YearsPreviousExperience: int
    InternalCode: int
    


class Usuario(BaseModel):
    UserId: int
    FirstName: str
    LastName: str
    Currency: str
    Email: str
    YearsPreviousExperience: int
    Skills: str
    InternalCode: int
    
    
    
class Empresa(BaseModel):
    Name: str
    City: str
    InternalCode: int
    

