from pydantic import BaseModel

class cultivoInput(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float

class cultivoOutput(BaseModel):
    prediction: str