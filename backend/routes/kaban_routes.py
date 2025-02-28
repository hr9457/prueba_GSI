from fastapi import APIRouter, FastAPI, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
import logging
from database.db import get_db
from controller.kanba_controller import create_kanban, get_kanba
from controller.stack_controller import get_stack, create_stack, get_all_stacks
from controller.task_controller import create_task, get_task, task_asigned_to

routes = APIRouter()


@routes.post('/kanban/{name_kanban}')
async def getTaks(name_kanban:str, db: AsyncSession = Depends(get_db)):
    logging.info('endpoint create kanban')   
    return await create_kanban(name_kanban,db)

@routes.get('/get_kanban')
async def getKanban(db: AsyncSession = Depends(get_db)):
    logging.info('endpoint get kanban')   
    return await get_kanba(db)


@routes.post('/taks/{name_stack}/{id_kanban}')
async def createTaks(name_stack:str, id_kanban:int, db: AsyncSession = Depends(get_db)):
    logging.info('POST CREATED TASK')
    return await create_stack(name_stack, id_kanban, db)

@routes.get('/get_stack/{id_stack}')
async def getTaks(id_stack:int, db: AsyncSession = Depends(get_db)):
    logging.info('endpoint get taks')
    return await get_stack(id_stack, db)


@routes.get('/get_all_stacks')
async def getAllStacks(db: AsyncSession = Depends(get_db)):
    logging.info('GET all stacks')
    return await get_all_stacks(db)



@routes.post('/task/{name_task}/{desc}/{asigned_to}/{id_stack}')
async def createTask(name_task:str, desc:str, asigned_to:str, id_stack:int, db: AsyncSession = Depends(get_db)):
    logging.info('GET all task')
    return await create_task(name_task,desc,asigned_to,id_stack,db)

@routes.get('/get_task/{id_task}')
async def getTask(id_task:int, db: AsyncSession = Depends(get_db)):
    logging.info('GET all task')
    return await get_stack(id_task,db)


@routes.get('/task_asigned/{id_stack}')
async def taskAsignedTo(id_stack:int,db: AsyncSession = Depends(get_db) ):
    logging.info('GET all tasks')
    return await task_asigned_to(id_stack, db)


@routes.get("/test_session")
async def test_session(db: AsyncSession = Depends(get_db)):
    print(f"Tipo de db: {type(db)}")  # Debería imprimir <class 'sqlalchemy.ext.asyncio.session.AsyncSession'>
    return {"message": "Revisar logs"}