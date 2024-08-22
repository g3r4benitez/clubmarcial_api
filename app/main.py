from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import init_db
from routers.alumno_router import router as alumno_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/algo')
def algo():
    print("Algo")
    return "Algo"

app.include_router(alumno_router)


if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)

