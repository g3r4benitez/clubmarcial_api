from http.client import HTTPException

from fastapi import Depends, FastAPI, Path
from contextlib import asynccontextmanager
from sqlmodel import Session, select

from alumno.alumno_model import Alumno
from database import init_db, get_session

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/alumno")
async def create_alumno(
        alumno_data: Alumno,
        sesion: Session = Depends(get_session)):
    alumno = Alumno(**alumno_data.model_dump())
    sesion.add(alumno)
    sesion.commit()
    sesion.refresh(alumno)
    return alumno

@app.get("/alumno/{alumno_id}")
async def get_alumno(
    #alumno_id: Annotated[int, Path(title="Alumno ID")],
    alumno_id: int,
    session: Session = Depends(get_session)
):
    alumno = session.get(Alumno, alumno_id)
    if alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no existe")
    return alumno

@app.get("/alumnos")
async def get_alumnos(
        session: Session = Depends(get_session)
):
    alumnos = session.exec(select(Alumno)).all()
    return alumnos

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)

