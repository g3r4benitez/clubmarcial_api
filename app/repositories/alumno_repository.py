from sqlmodel import Session

from app.models.alumno_model import Alumno

class AlumnoRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_alumno(self, alumno_id: int) -> Alumno:
        return self.session.get(Alumno, alumno_id)
