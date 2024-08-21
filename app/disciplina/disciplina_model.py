from typing import Optional
from sqlmodel import Field, SQLModel


class Disciplina(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    valor_mes: float
    valor_clase: float


class Alumno_disciplinea(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    alumno_id: int
    disciplina_id: int
