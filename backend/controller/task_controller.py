
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import json
import logging


async def create_task(name_task:str, desc: str, asigned_to:str, id_stack:int, db:AsyncSession):
    try:
        query = text('INSERT INTO taks(name_task, description, asigned_to, id_stack) VALUES(:name_task,:description,:asigned_to,:id_stack)')
        await db.execute(query, {'name_task':name_task, 'description':desc, 'asigned_to':asigned_to, 'id_stack':id_stack})
        await db.commit()
        logging.info('Created to new task')
        return JSONResponse(
            status_code=201,
            content={"message": "Task creado exitosamente", "name_taks": name_task}
        )
    except Exception as e:
        logging.error('Not Created Task on DB')
        raise HTTPException(
            status_code=404,
            detail=f'No se logró crear el Stack {name_task}. Error: {str(e)}'
        )
    


async def get_task(id_task:int, db:AsyncSession):
    try:
        query = text(f"SELECT * FROM taks WHERE id_task={id_task}")
        res = await db.execute(query)
        result = res.fetchone()
        print(result)
        logging.info('Search new Task')
        return JSONResponse(
            status_code=200,
            content={"data": {
                'id_task': result[0],
                'name_task': result[1],
                'description': result[2],
                'asigned_to': result[3],
                'id_stack': result[4]
            }}
        )
    except Exception as e:
        logging.error('Not Find Task on DB')
        raise HTTPException(
            status_code=404,
            detail=f'No se logró Obtener Task {id_task}. Error: {str(e)}'
        )



async def task_asigned_to(id_stack:int, db:AsyncSession):
    try:
        query = text(f"SELECT * FROM taks WHERE id_stack={id_stack}")
        res = await db.execute(query)
        result = res.fetchall()
        print(result)
        logging.info('Search new Task')
        list_of_taks = [{'id_task':item[0], 'name_task':item[1], 'description':item[2], 'asigned_to':item[3], 'id_stack':item[4]} for item in result ]
        return JSONResponse(
            status_code=200,
            content={"data":list_of_taks}
        )
    except Exception as e:
        logging.error('Not Find tasks on DB')
        raise HTTPException(
            status_code=404,
            detail=f'No se logró Obtener Task {id_stack}. Error: {str(e)}'
        )