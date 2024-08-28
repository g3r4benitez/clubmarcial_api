from sqlmodel import Session

from models.alumno_model import Alumno

class AlumnoRepository:
    def __init__(self, session: Session):
        self.session = session

    async def get_alumno(self, alumno_id: int) -> Alumno:
        return self.session.get(Alumno, alumno_id)

    def create_alumno(self, alumno: Alumno):
        self.session.add(alumno)
        self.session.commit()
        self.session.refresh(alumno)
        return alumno
