from tortoise.contrib.fastapi import register_tortoise

from fastapi import FastAPI

from starlette.middleware.sessions import SessionMiddleware

from core.config import SECRET_KEY, DATABASE_URL, APPS_MODELS
from routers import routers

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

register_tortoise(
    app=app,
    db_url=DATABASE_URL,
    modules={'models': APPS_MODELS},
    generate_schemas=False,
    add_exception_handlers=True
)

app.include_router(routers)
