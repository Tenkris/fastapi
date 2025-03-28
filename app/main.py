from fastapi import FastAPI
from app.routers import books, auth, users, question
from fastapi.middleware.cors import CORSMiddleware
from app.utils.db import init_db

app = FastAPI()

origins = [
    # ConfigFRONTEND_URL,
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
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(users.router, prefix='/api/v1/users', tags=["users"])
app.include_router(question.router, prefix='/api/v1/questions', tags=["questions"]) 