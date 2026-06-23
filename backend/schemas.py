from pydantic import BaseModel
from typing import Optional
from datetime import date

# ==========================================
# SCHEMAS (VALIDADORES DE LA API)
# ==========================================

# 1. Esquema Base: Los datos básicos que siempre lleva una meta
class MetaBase(BaseModel):
    nombre: str
    costo_total: float
    fecha_objetivo: Optional[date] = None

# 2. Esquema para CREAR (Lo que el usuario envía desde el dashboard)
class MetaCreate(MetaBase):
    usuario_id: int

# 3. Esquema de RESPUESTA (Lo que la API devuelve desde la Base de Datos)
class MetaResponse(MetaBase):
    id: int
    ahorrado_actual: float
    estado: str

    class Config:
        # Esto permite que Pydantic lea la información directo de SQLAlchemy
        from_attributes = True
        
# ==========================================
# SCHEMAS PARA USUARIOS
# ==========================================
class UsuarioBase(BaseModel):
    nombre: str
    correo: str

class UsuarioCreate(UsuarioBase):
    pass  # De momento pide lo mismo que la base

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True