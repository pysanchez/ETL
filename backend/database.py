from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ==========================================
# CREDENCIALES DEL SISTEMA IGM
# ==========================================

URL_BASE_DATOS = "postgresql://postgres:devsanchez@localhost:5432/sistemaigm"

# El "engine" es el motor que mantiene la conexión viva con PostgreSQL
engine = create_engine(URL_BASE_DATOS)

# SessionLocal es lo que usaremos para abrir "ventanas" de transacciones a la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base es la clase madre de la que heredarán todos nuestros modelos
Base = declarative_base()