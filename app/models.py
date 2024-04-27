from sqlmodel import Field, SQLModel

class Contract(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=True)
    content: str

class Hypothesis(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    content: str

class ContractHypothesis(SQLModel, table=True):
    id: int = Field(primary_key=True)
    contract_id: int = Field(foreign_key="contract.id")
    hypothesis_id: int = Field(foreign_key="hypothesis.id")
    label: str = Field(default=None)