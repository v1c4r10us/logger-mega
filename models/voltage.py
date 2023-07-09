from pydantic import BaseModel

class Voltage(BaseModel):
    date: str
    time: str
    s_1: float
    s_2: float
    s_3: float
    s_4: float
    s_5: float
