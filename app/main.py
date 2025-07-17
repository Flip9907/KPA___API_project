from fastapi import FastAPI
from . import models
from .database import engine
from .routers import get_methods,post_methods

app=FastAPI()

try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print(e)


app.include_router(get_methods.router)
app.include_router(post_methods.router)
