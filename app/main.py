from fastapi import FastAPI
from app.routers import proyectos

app = FastAPI()
app.include_router(proyectos.router)
