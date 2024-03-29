from fastapi import FastAPI
from app.router import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "UPDATE"],
    allow_headers=["*"],
)

@app.get("/") 
def read_root(): 
    return {"Hello" : "World"}

app.include_router(router)
