from database import engine, Base
import models 

print("⏳ Conectando con PostgreSQL...")

try:
    Base.metadata.create_all(bind=engine)
    print("✅ ¡Éxito! Todas las tablas del Sistema IGM han sido creadas en la base de datos.")
except Exception as e:
    print(f"❌ Hubo un error al conectar: {e}")