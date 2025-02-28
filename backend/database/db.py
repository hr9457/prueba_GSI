from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
import logging
import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql+asyncpg://root:root@192.168.57.130:5432/mydatabase"

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


