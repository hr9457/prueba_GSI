# controllers/kanban_controller.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import json
import logging


async def create_kanban(name_kanban: str, db: AsyncSession):
    try:
        query = text("INSERT INTO kanban (name_kanban) VALUES (:name_kanban)")
        await db.execute(query, {"name_kanban": name_kanban})
        await db.commit()
        logging.info('Created new Kanban')
        return JSONResponse(
            status_code=201,
            content={"message": "Kanban creado exitosamente", "name_kanban": name_kanban}
        )
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f'No se logró crear el kanban {name_kanban}. Error: {str(e)}'
        )
    

async def get_kanba(db:AsyncSession):
    try:
        query = text("SELECT * FROM kanban")
        res = await db.execute(query)
        result = res.fetchall()
        list_of_kanba = [{'id_kanban':item[0], 'kanban_name':item[1]} for item in result ]
        logging.info('Created list kanban and converted in json')
        return JSONResponse(
            status_code=201,
            content={"data": list_of_kanba}
        )
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f'Error Interno Servidors'
        )