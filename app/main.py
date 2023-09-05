from fastapi import FastAPI
from .routers import posts, signup, login

app = FastAPI()

app.include_router(signup.router)
app.include_router(login.router)
app.include_router(posts.router)