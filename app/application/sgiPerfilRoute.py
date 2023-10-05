from infrastructure.outputadapter.Database import Base, engine, localSession
from fastapi import APIRouter, Depends, HTTPException
from domain.sgiPerfil import schemas
from sqlalchemy.orm import Session
from application import sgiPerfilService

Base.metadata.create_all(bind=engine)
def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

#ruta
sgiPerfil_ruta = APIRouter()
#--------------------- PERFIL -----------------
#crear
@sgiPerfil_ruta.post("/sgiPerfil/crear")
def ingresar_perfil(perfil: schemas.PerfilEsquema, db: Session = Depends(get_db)):
    return sgiPerfilService.crear_perfil(db=db,perfil=perfil)
#listar todos
@sgiPerfil_ruta.get("/sgiPerfil")
def obtenet_todos_perfiles(db: Session = Depends(get_db)):
    return sgiPerfilService.get_perfiles_todos(db=db)
#editar
@sgiPerfil_ruta.put("/sgiPerfil/editar/{id}")
def actualizar_perfil(id, perfil_esquema: schemas.PerfilEsquema, db: Session = Depends(get_db)):
    obj = sgiPerfilService.editar_perfil(db=db, id=id, perfil_esquema=perfil_esquema)
    if obj:
        return obj
    raise HTTPException(status_code=404, detail=' Idioma not Found!!')
#eliminar
@sgiPerfil_ruta.delete("/sgiPerfil/eliminar/{id}")
def eliminar_perfil(id, db: Session = Depends(get_db)):
    sgiPerfilService.delete(db=db, id=id)