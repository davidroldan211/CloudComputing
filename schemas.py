from pydantic import BaseModel
from typing import List, Optional

class MLModelBase(BaseModel):
    learning_rate: float
    epochs: int
    batch_size: int
    neurons: List[int]
    weights: List[float]
    biases: List[float]

class MLModelCreate(MLModelBase):
    id: str

class MLModel(MLModelBase):
    id: str

    class Config:
        orm_mode = True
