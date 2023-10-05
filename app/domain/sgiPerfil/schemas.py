from pydantic import BaseModel

class PerfilEsquema(BaseModel):
    nombre: str
    descripcion: str

class PerfilIdEsquema(PerfilEsquema):
    id: int