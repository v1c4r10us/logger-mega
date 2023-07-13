from pydantic import BaseModel
from typing import Optional

class Voltage(BaseModel):
    date: Optional[str]
    time: Optional[str]
    s_1: float
    s_2: float
    s_3: float
    s_4: float
    s_5: float
    s_6: float
    s_7: float
    s_8: float
    s_9: float
    s_10: float
    s_11: float
    c_1: float
