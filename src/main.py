import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.core import config
from src.core.logger import LOGGING
from src.api.v1 import base, entity
from src.core.config import app_settings

app = FastAPI(
    title=app_settings.app_title,   # название приложение берём из настроек
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)

app.include_router(base.api_router, prefix="/api/v1")
#app.include_router(entity.router, prefix="/api/v1")

if __name__ == '__main__':
    # Приложение может запускаться командой
    # `uvicorn main:app --host 0.0.0.0 --port 8080`
    # но чтобы не терять возможность использовать дебагер,
    # запустим uvicorn сервер через python
    uvicorn.run(
        'main:app',
        host=config.PROJECT_HOST,
        port=config.PROJECT_PORT,
    )