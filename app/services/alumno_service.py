from fastapi import Depends
from sqlmodel import Session

from repositories.alumno_repository import AlumnoRepository
from models.alumno_model import Alumno
from core.database import get_session

class AlumnoService:
    #def __init__(self, alumno_repository: AlumnoRepository):
    #    self.alumno_repository = alumno_repository
    #
    #async def get_alumno(self, alumno_id: int):
    #    return await self.alumno_repository.get_alumno(alumno_id)
    #
    # async def create_alumno(self, alumno: Alumno):
    #     return self.alumno_repository.create_alumno(alumno)

    async def get_alumno(
            self,
            alumno_id: int,
            session: Session = Depends(get_session)
    ):
        #session = get_session()
        return session.get(Alumno, alumno_id)