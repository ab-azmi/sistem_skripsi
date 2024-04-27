from fastapi import APIRouter, Depends
from app.db import  get_session
from app.models import Contract, Hypothesis, ContractHypothesis, Label
from fastapi import UploadFile, File
import json

router = APIRouter(
    prefix="/contracts",
    tags=["Contracts"]
)

@router.post("/")
async def create_contract(contract: Contract, session = Depends(get_session)):
    session.add(contract)
    session.commit()
    session.refresh(contract)
    return contract

@router.get("/")
async def read_contracts(session = Depends(get_session)) -> list[Contract]:
    return session.query(Contract).all()

@router.post("/import")
async def import_contracts(file: UploadFile = File(), session = Depends(get_session)):
    contracts = await file.read()
    # Process the contracts data
    contracts = json.loads(contracts)
    contracts = [Contract(
        content=contract['premise'],
    ) for contract in contracts]

    session.add_all(contracts)
    session.commit()
    return 'Contracts imported successfully'