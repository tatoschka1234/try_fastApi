import sys
from fastapi import APIRouter
from typing import Optional, Union
from .entity import router
from typing import Optional

# Объект router, в котором регистрируем обработчики
api_router = APIRouter()
api_router.include_router(router, prefix="/entities", tags=["entities"])


@api_router.get('/info')
async def info_handler():
    return {
        'api': 'v1',
        'python': sys.version_info
    }


@api_router.get('/{action}')
async def action_handler(action):
    return {
        'action': action
    }


@api_router.get('/filter')
async def filter_handler(
    param1: str,
    param2: Optional[int] = None,
) -> dict[str, Union[str, int, None]]:
    return {
        'action': 'filter',
        'param1': param1,
        'param2': param2
    }