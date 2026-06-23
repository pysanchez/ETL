from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# Importaciones de tu arquitectura local
from database import engine, SessionLocal
import models
import schemas

# Esto crea las tablas en la base de datos local automáticamente si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Sistema IGM (Ingresos, Gastos, Metas)")

# Dependencia de seguridad para abrir y cerrar la conexión a la base de datos en cada petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al Backend del Sistema IGM"}

# --- ENDPOINTS DE INGRESOS ---
@app.get("/ingresos/")
def obtener_ingresos(db: Session = Depends(get_db)):
    # Aquí irá la lógica para consultar los ingresos desde PostgreSQL
    return {"status": "Endpoint de ingresos funcionando y a la espera de datos"}

# --- ENDPOINTS DE GASTOS ---
@app.get("/gastos/")
def obtener_gastos(db: Session = Depends(get_db)):
    # Aquí irá la lógica para consultar los gastos
    return {"status": "Endpoint de gastos funcionando y a la espera de datos"}

# --- ENDPOINTS DE METAS ---
@app.get("/metas/")
def obtener_metas(db: Session = Depends(get_db)):
    # Aquí irá la lógica para revisar el progreso de tus metas
    return {"status": "Endpoint de metas de ahorro funcionando y a la espera de datos"}