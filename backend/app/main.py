import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

from fastapi import FastAPI
from app.routers import users, auth

app = FastAPI()

# Підключення маршрутів
app.include_router(users.router)
app.include_router(auth.router)
