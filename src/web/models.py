from datetime import datetime
from pydantic import BaseModel

class Status(BaseModel):
    is_complited: bool
    description: str
    

class Student(BaseModel):
    name: str
    surname: str
    group: str | None
    

class Text(BaseModel):
    id: int
    student: Student | None
    text: list[str]
    status: Status
    created_at: datetime
    
class Metrics(BaseModel):
    UNIQ_W_PROPORTION: float = 0
    ORTHOGRAPHY_ERRORS: float = 0
    COLLOQUIAL_WORDS: float = 0
    COLLOCATION_ERRORS: float = 0
    A1_PROPORTION: float = 0
    A2_PROPORTION: float = 0
    B1_PROPORTION: float = 0
    B2_PROPORTION: float = 0
    C1_PROPORTION: float = 0
    C2_PROPORTION: float = 0
    
class Response(BaseModel):
    CA1: float = 0
    CA11: float = 0
    CA12: float = 0
    CA13: float = 0
    CA14: float = 0
    CA15: float = 0
    CA16: float = 0
    CA17: float = 0
    CA2: float = 0
    ORG1: float = 0
    ORG2: float = 0
    ORG22: float = 0
    ORG23: float = 0
    ORG24: float = 0
    ORG25: float = 0
    ORG3: float = 0
    VOC1: float = 0
    VOC2: float = 0
    VOC3: float = 0
    GR1: float = 0
    GR2: float = 0
    GR3: float = 0
    metrics: Metrics