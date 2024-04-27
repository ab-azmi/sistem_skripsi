from fastapi import APIRouter, Depends
from app.db import  get_session
from app.models import ContractHypothesis, Contract, Hypothesis
import torch
from transformers import AlbertTokenizer, AlbertForSequenceClassification
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, TensorDataset
from torch.nn.functional import softmax

router = APIRouter(
    prefix="/model",
    tags=["Model"]
)

#analyze take contract_id and hypothesis_id and return the label
@router.post("/analyze")
async def analyze(contract_id: int, hypothesis_id: int, session = Depends(get_session)):

    #check if pair already exist
    pair = session.query(ContractHypothesis).filter_by(contract_id=contract_id, hypothesis_id=hypothesis_id).first()
    if pair is not None:
        #return the pair
        return pair

    model = AlbertForSequenceClassification.from_pretrained("albert-base-v2", num_labels=3)

    #import pth file
    state_dict = torch.load('BS8_WM0_HG1_EP10_LR2e-05_ESTrue_S444.pth')
    model.load_state_dict(state_dict)

    #get contract and hypothesis content
    contract = session.query(Contract).get(contract_id).content
    hypothesis = session.query(Hypothesis).get(hypothesis_id).content


    tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
   
   # Encode contract and hypothesis
    contract_encoded = tokenizer.encode(contract, add_special_tokens=False)
    hypothesis_encoded = tokenizer.encode(hypothesis, add_special_tokens=False)

    # Create token IDs, segment IDs, and attention mask IDs
    token_ids = torch.tensor([tokenizer.cls_token_id] + contract_encoded + [tokenizer.sep_token_id] + hypothesis_encoded + [tokenizer.sep_token_id]).unsqueeze(0)
    segment_ids = torch.tensor([0] * (len(contract_encoded) + 2) + [1] * (len(hypothesis_encoded) + 1)).unsqueeze(0)
    attention_mask_ids = torch.tensor([1] * (len(contract_encoded) + len(hypothesis_encoded) + 3)).unsqueeze(0)

    # Feed token IDs, segment IDs, and attention mask IDs into model
    outputs = model(input_ids=token_ids, token_type_ids=segment_ids, attention_mask=attention_mask_ids)

    # Get the model's prediction
    predictions = softmax(outputs.logits, dim=1)
    _, predicted_label = torch.max(predictions, 1)
    
    #label dict
    label_dict = {0: 'entail', 1: 'contradict', 2: 'neutral'}
    
    contract_hypothesis = ContractHypothesis(contract_id=contract_id, hypothesis_id=hypothesis_id, label=label_dict[predicted_label.item()])

    session.add(contract_hypothesis)
    session.commit()
    session.refresh(contract_hypothesis)
    #return success message
    return contract_hypothesis

@router.post("/run/{subset}")
async def run(subset: str, session = Depends(get_session)):
    # This is where the magic happens
    return 'Done'