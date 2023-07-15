from fastapi import FastAPI
from routes.user_routes import UsersRouter

description=""

app = FastAPI(
    title="Gordian",
    version="v1.0",
    description=description,
    redoc_url=None
)

app.include_router(UsersRouter)