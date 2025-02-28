from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
import logging
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
NAME = os.getenv("NAME")
USER = os.getenv("USER")
PASS = os.getenv("PASS")

DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASS}@{HOST}:{PORT}/{NAME}"

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


