from fastapi import APIRouter, Depends
from app.db import  get_session
from app.models import ContractHypothesis, Contract, Hypothesis
from app.utils.predict import predict
from pydantic import BaseModel

router = APIRouter(
    prefix="/model",
    tags=["Model"]
)

class Pair(BaseModel):
    contract: str
    hypothesis: str

#analyze take contract_id and hypothesis_id and return the label
@router.post("/analyze")
async def analyze(contract_id: int, hypothesis_id: int, session = Depends(get_session)):

    #check if pair already exist
    pair = session.query(ContractHypothesis).filter_by(contract_id=contract_id, hypothesis_id=hypothesis_id).first()
    if pair is not None:
        #return the pair
        return pair
    
    #get contract and hypothesis content
    contract = session.query(Contract).get(contract_id).content
    hypothesis = session.query(Hypothesis).get(hypothesis_id).content

    #predict the label
    result = predict(hypothesis, contract)
    
    contract_hypothesis = ContractHypothesis(contract_id=contract_id, hypothesis_id=hypothesis_id, label=result)

    session.add(contract_hypothesis)
    session.commit()
    session.refresh(contract_hypothesis)
    #return success message
    return contract_hypothesis

@router.post("/customanalyze")
async def customanalyze(pair: Pair, session = Depends(get_session)):
    #get contract and hypothesis content
    contract = pair.contract
    hypothesis = pair.hypothesis
    #predict the label
    result = predict(hypothesis, contract)
    return result

@router.post("/run/{subset}")
async def run(subset: str, session = Depends(get_session)):
    # This is where the magic happens
    return 'Done'