from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel

class Proyecto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    descripcion: str
    imagen_url: str
    demo_url: Optional[str] = None
    repositorio_url: Optional[str] = None
    tecnologias: str

class ContactoForm(BaseModel):
    nombre: str
    email: str
    servicio: str
    mensaje: str