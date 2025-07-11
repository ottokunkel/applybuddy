from fastapi import APIRouter
from src.models.fields import FieldCreateRequest, FieldCreateResponse
from src.core.field_service import create_field

router = APIRouter()

@router.post("/", response_model=FieldCreateResponse)
async def create(field: FieldCreateRequest):
    """ Create a new field with question and answer """
    field_id = create_field(field.question, field.answer)
    return FieldCreateResponse(
        field_id=field_id,
        message="Field created successfully"
    )

@router.get("/")
async def query(query: str):
    # TODO: implement field querying
    return {"message": "Field queried"}