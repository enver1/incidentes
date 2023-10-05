from fastapi import FastAPI
from app.application import sgiPerfilRoute
app = FastAPI()
app.include_router(sgiPerfilRoute.sgiPerfil_ruta)