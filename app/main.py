from fastapi import FastAPI, Depends
from app.db import init_db, get_session
from app.models import Contract, Hypothesis, ContractHypothesis, Label

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/hypothesis")
async def create_hypothesis(hypothesis: Hypothesis, session = Depends(get_session)):
    session.add(hypothesis)
    session.commit()
    session.refresh(hypothesis)
    return hypothesis

@app.get("/hypothesis")
async def read_hypotheses(session = Depends(get_session)) -> list[Hypothesis]:
    return session.query(Hypothesis).all()

@app.post("/hypothesis/import")
async def import_hypotheses(hypotheses: list[Hypothesis], session = Depends(get_session)):
    session.add_all(hypotheses)
    session.commit()
    return hypotheses

@app.post("/contracts")
async def create_contract(contract: Contract, session = Depends(get_session)):
    session.add(contract)
    session.commit()
    session.refresh(contract)
    return contract

@app.get("/contracts")
async def read_contracts(session = Depends(get_session)) -> list[Contract]:
    return session.query(Contract).all()

#analyze take contract_id and hypothesis_id and return the label
@app.post("/analyze")
async def analyze(contract_id: int, hypothesis_id: int, session = Depends(get_session)):
    contract_hypothesis = ContractHypothesis(contract_id=contract_id, hypothesis_id=hypothesis_id)

    # This is where the magic happens
    

    session.add(contract_hypothesis)
    session.commit()
    return contract_hypothesis.label
