from typing import Optional
from sqlmodel import Field, SQLModel

class Alumno(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    #fechanac: datetime.date
    sexo: str
    dni: Optional[int]
    telefono: Optional[int]
    peso: Optional[float]
    foto_perfil: Optional[str]
    is_active: bool = True

