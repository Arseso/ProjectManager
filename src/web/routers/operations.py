from typing import List
from fastapi import APIRouter
from src.web.models import Text
router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)

@router.get('/texts/search/{search_request}')
async def search(search_request: str):
    # Search by request 
    raise NotImplementedError
    
@router.post('/submit/{texts}')
async def submit(texts: List[Text]):
    raise NotImplementedError

@router.get('/texts')
async def get_texts() -> List[Text]:
    raise NotImplementedError

@router.get('/texts/{id}')
async def get_text_info(id: int) -> Text:
    raise NotImplementedError