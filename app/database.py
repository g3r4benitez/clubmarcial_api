import os
from sqlmodel import create_engine, Session, SQLModel

from alumno.alumno_model import Alumno
from disciplina.disciplina_model import Disciplina, Alumno_disciplinea

SQLALCHEMY_DATABASE_URL = os.environ.get("DB_URL")
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

def init_db():
    print("Executing init db")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

