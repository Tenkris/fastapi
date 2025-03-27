from fastapi import FastAPI
from app.routers import books
from fastapi.middleware.cors import CORSMiddleware
from app.utils.db import init_db

app = FastAPI()

origins = [
    # Config.FRONTEND_URL,
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(books.router, prefix='/api/v1/books', tags=["books"])