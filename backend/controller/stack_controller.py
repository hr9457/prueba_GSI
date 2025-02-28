# controllers/kanban_controller.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import json
import logging


async def create_stack(name_stack: str, id_kanban:int, db: AsyncSession):
    try:
        query = text("INSERT INTO stack (name_stack, id_kanban) VALUES (:name_stack, :id_kanban)")
        await db.execute(query, {"name_stack": name_stack, "id_kanban":id_kanban})
        await db.commit()
        logging.info('Created new Stack')
        return JSONResponse(
            status_code=201,
            content={"message": "Stack creado exitosamente", "name_stack": name_stack}
        )
    except Exception as e:
        logging.error('Not Created Stack on DB')
        raise HTTPException(
            status_code=404,
            detail=f'No se logró crear el Stack {name_stack}. Error: {str(e)}'
        )
    


async def get_stack(id_stack:int, db: AsyncSession):
    try:
        query = text(f"SELECT * FROM stack WHERE id_stack={id_stack}")
        res = await db.execute(query)
        result = res.fetchone()
        print(result)
        logging.info('Created new Stack')
        return JSONResponse(
            status_code=200,
            content={"data": {
                'id_stack': result[0],
                'name_stack': result[1],
                'id_kanban': result[2]
            }}
        )
    except Exception as e:
        logging.error('Not Created Stack on DB')
        raise HTTPException(
            status_code=404,
            detail=f'No se logró Obtener Satack {id_stack}. Error: {str(e)}'
        )
    


async def get_all_stacks(db: AsyncSession):
    try:
        query = text("SELECT * FROM stack")
        res = await db.execute(query)
        result = res.fetchall()
        logging.info('GET all stacks')
        list_of_stacks = [{'id_stack':item[0], 'stack_name':item[1]} for item in result ]
        return JSONResponse(
            status_code = 200,
            content={
                'data': list_of_stacks
            }
        )

    except Exception as e:
        logging.error('Not Response get all stacks')
        raise HTTPException(
            status_code=404,
            detail=f'Error Interno Servidor'
        )