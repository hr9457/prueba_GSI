from fastapi import APIRouter, FastAPI

routes = APIRouter()


@routes.get('/taks')
def getTaks():
    return 'taks'