from sqlalchemy import Column, Integer, String, ForeignKey
from infrastructure.outputadapter.Database import Base
from sqlalchemy.orm import relationship

class sgiPerfil(Base):
    __tablename__ = 'sgiPerfil'
    idSgiPerfil = Column( Integer, primary_key=True)
    nombre = Column(String(100))     
    descripcion = Column(String(100))   