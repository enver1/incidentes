from sqlalchemy.orm import Session
from domain.sgiPerfil import schemas, models
from application import util
from fastapi import HTTPException

#Tabla sgiPerfil
#create
def crear_perfil(db: Session, perfil: schemas.PerfilEsquema):
     obj = models.sgiPerfil(nombre=perfil.nombre, descripcion=perfil.descripcion)
     db.add(obj)
     db.commit()
     db.flush(obj)
     return obj
#obtener los primeros 100 registros
def get_perfiles_limit(db: Session, skip: int = 0, limit: int = 100, ):
    return db.query(models.sgiPerfil).offset(skip).limit(limit).all()
#obtener todos los perfiles
def get_perfiles_todos(db: Session):
    return db.query(models.sgiPerfil).all()
#buscar por id
def get_idioma_por_id(db: Session, id: int):
    return db.query(models.sgiPerfil).filter(models.sgiPerfil.idSgiPerfil == id).first()
#editar
def editar_perfil(db: Session, id: int, perfil_esquema: schemas.PerfilEsquema):
    obj = get_idioma_por_id(db, id=id)
    if(obj.idSgiPerfil):
        obj.nombre=perfil_esquema.nombre
        obj.descripcion=perfil_esquema.descripcion
        db.commit()
        db.refresh(obj)
        return obj
#eliminar
def delete(db: Session, id: int):
    obj = get_idioma_por_id(db, id=id)
    if obj is None:
        raise HTTPException(status_code=404, detail=util.addErrorMessage_DOES_NOT_EXIST)
    return remove_idioma(db, obj_idioma=obj)
def remove_idioma(db: Session, obj_idioma: models.sgiPerfil):
    db.delete(obj_idioma)
    db.commit()
    return True