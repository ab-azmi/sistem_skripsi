from fastapi import APIRouter, Depends
from app.db import  get_session
from app.models import ContractHypothesis, Contract, Hypothesis
import torch
from transformers import AlbertTokenizer

router = APIRouter(
    prefix="/model",
    tags=["Model"]
)

#analyze take contract_id and hypothesis_id and return the label
@router.post("/analyze")
async def analyze(contract_id: int, hypothesis_id: int, session = Depends(get_session)):
    contract_hypothesis = ContractHypothesis(contract_id=contract_id, hypothesis_id=hypothesis_id)

    #import pth file
    model = torch.load('BS8_WM0_HG1_EP10_LR2e-05_ESTrue_S444.pth')

    #get contract and hypothesis content
    contract = session.query(Contract).get(contract_id).content
    hypothesis = session.query(Hypothesis).get(hypothesis_id).content

    tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
    #encode contract and hypothesis
    contract_encoded = tokenizer.encode(contract, return_tensors='pt', max_length=512, truncation=True)
    hypothesis_encoded = tokenizer.encode(hypothesis, return_tensors='pt', max_length=512, truncation=True)

    #pair token ids contract and hypothesis
    pair_token_id = [tokenizer.cls_token_id] + contract_encoded + [tokenizer.sep_token_id] + hypothesis_encoded + [tokenizer.sep_token_id]

    #predict
    model.eval()
    with torch.no_grad():
        output = model(torch.tensor(pair_token_id).unsqueeze(0))
        label = torch.argmax(output.logits).item()
        if label == 0:
            contract_hypothesis.label = 'entail'
        elif label == 1:
            contract_hypothesis.label = 'contradict'
        else:
            contract_hypothesis.label = 'neutral'
    

    # session.add(contract_hypothesis)
    # session.commit()
    return contract_hypothesis

@router.post("/run/{subset}")
async def run(subset: str, session = Depends(get_session)):
    # This is where the magic happens
    return 'Done'