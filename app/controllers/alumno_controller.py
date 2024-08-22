from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from http.client import HTTPException

from models.alumno_model import Alumno
from core.database import get_session


router = APIRouter()

@router.post("/")
async def create_alumno(
        alumno_data: Alumno,
        sesion: Session = Depends(get_session)):
    alumno = Alumno(**alumno_data.model_dump())
    sesion.add(alumno)
    sesion.commit()
    sesion.refresh(alumno)
    return alumno

@router.get("/{alumno_id}", response_model=Alumno)
async def get_alumno(
    alumno_id: int,
    session: Session = Depends(get_session)
):
    alumno = session.get(Alumno, alumno_id)
    if alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no existe")
    return alumno

@router.get("/")
async def get_alumnos(
        session: Session = Depends(get_session)
):
    alumnos = session.exec(select(Alumno)).all()
    return alumnos

