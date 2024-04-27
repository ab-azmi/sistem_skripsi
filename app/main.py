from fastapi import FastAPI, Depends
from app.db import  get_session
from app.models import ContractHypothesis
from app.routers import hypothesis, contracts, ml
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(hypothesis.router)

app.include_router(contracts.router)

app.include_router(ml.router)
