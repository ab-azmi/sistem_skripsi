from sqlmodel import Field, SQLModel
from enum import Enum

class Contract(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=True)
    content: str

class Hypothesis(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    content: str

class Label(Enum):
    ENTAIL = "entail"
    CONTRADICT = "contradict"
    NEUTRAL = "neutral"

class ContractHypothesis(SQLModel, table=True):
    id: int = Field(primary_key=True)
    contract_id: int = Field(foreign_key="contract.id", primary_key=True)
    hypothesis_id: int = Field(foreign_key="hypothesis.id", primary_key=True)
    label: Label = Field(nullable=True)