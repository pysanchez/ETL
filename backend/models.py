from sqlalchemy import Column, Integer, String, Numeric, Date, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

# ==========================================
# MODELOS DE LA BASE DE DATOS (SISTEMA IGM)
# ==========================================

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    creado_en = Column(DateTime, default=func.now())

    # Relaciones bidireccionales
    categorias = relationship("Categoria", back_populates="usuario")
    transacciones = relationship("Transaccion", back_populates="usuario")
    metas = relationship("Meta", back_populates="usuario")

class Categoria(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    nombre = Column(String(50), nullable=False)
    tipo = Column(String(20), CheckConstraint("tipo IN ('ingreso', 'gasto')"), nullable=False)

    usuario = relationship("Usuario", back_populates="categorias")
    transacciones = relationship("Transaccion", back_populates="categoria")

class Transaccion(Base):
    __tablename__ = "transacciones"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id", ondelete="RESTRICT"), nullable=False)
    monto = Column(Numeric(10, 2), nullable=False)
    fecha = Column(Date, nullable=False)
    concepto = Column(String(255), nullable=False)
    creado_en = Column(DateTime, default=func.now())

    usuario = relationship("Usuario", back_populates="transacciones")
    categoria = relationship("Categoria", back_populates="transacciones")

class Meta(Base):
    __tablename__ = "metas"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    nombre = Column(String(100), nullable=False)
    costo_total = Column(Numeric(10, 2), nullable=False)
    ahorrado_actual = Column(Numeric(10, 2), default=0.00)
    fecha_objetivo = Column(Date)
    estado = Column(String(20), default="en_progreso")

    usuario = relationship("Usuario", back_populates="metas")