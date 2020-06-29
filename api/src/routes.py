from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def path_main():
    return {'msg': 'Hello world!'}
