from fastapi import APIRouter
from controllers.alumno_controller import router as alumno_router

router = APIRouter()

# Importa las rutas definidas en el controlador
router.include_router(alumno_router, prefix="/alumnos", tags=["alumnos"])

# Aquí podrías definir otras rutas específicas de usuarios si lo necesitas

# Exporta el router para que pueda ser utilizado en el archivo principal de rutas
__all__ = ["router"]