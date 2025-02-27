from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
import logging

DATABASE_URL = "postgresql+asyncpg://root:root@192.168.57.130:5432/mydatabase"

# asincrono
engine = create_async_engine(DATABASE_URL, echo=True)

# config
Base = declarative_base()
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,  # Usamos sesiones asíncronas
    expire_on_commit=False
)

# session conexion
async def get_db():
    logging.info('Creando conexion a la base de datos')
    async with SessionLocal() as session:
        logging.info('Cerrando conexion a la base de datos')
        yield session


