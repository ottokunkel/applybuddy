from pydantic import BaseModel
from typing import Optional


class FieldCreateRequest(BaseModel):
    question: str
    answer: str


class FieldCreateResponse(BaseModel):
    field_id: str
    message: str 