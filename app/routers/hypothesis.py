from fastapi import APIRouter, Depends
from app.db import  get_session
from app.models import Contract, Hypothesis, ContractHypothesis

router = APIRouter(
    prefix="/hypothesis",
    tags=["Hypothesis"]
)

@router.post("/")
async def create_hypothesis(hypothesis: Hypothesis, session = Depends(get_session)):
    session.add(hypothesis)
    session.commit()
    session.refresh(hypothesis)
    return hypothesis

@router.get("/")
async def read_hypotheses(session = Depends(get_session)) -> list[Hypothesis]:
    return session.query(Hypothesis).all()

@router.post("/import", response_model=list[Hypothesis])
async def import_hypotheses(hypotheses: list[Hypothesis], session = Depends(get_session)):
    session.add_all(hypotheses)
    session.commit()
    for hypothesis in hypotheses:
        session.refresh(hypothesis)
    return hypotheses