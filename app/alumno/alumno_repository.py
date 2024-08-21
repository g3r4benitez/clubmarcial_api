from sqlalchemy.exc import IntegrityError
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session

from alumno_model import Alumno
from alumno_schema import AlumnoSchema

def get(_id: int):
    return db.session.query(Alumno).filter(Alumno.id == _id).first()

def create(db: Session, alumno: AlumnoSchema):
    db_alumno = Alumno(**alumno.model_dump())
    db.add(db_alumno)
    db.commit()
    db.refresh((db_alumno))
    return db_alumno

