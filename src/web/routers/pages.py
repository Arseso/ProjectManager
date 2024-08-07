from typing import List
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from src.web.models import Text

router_base = APIRouter(
    prefix=''
)

router_texts = APIRouter(
    prefix='/texts'
)


templates = Jinja2Templates(directory='/templates')

@router_base.get('/')
async def get_base(request: Request):
    return templates.TemplateResponse("base.html", {'request': request, 'texts': List[Text]})

@router_texts.get('/')
async def get_texts(request: Request):
    return templates.TemplateResponse("texts_list.html", {'request': request, 'texts': List[Text]})

@router_texts.get('/upload/')
async def upload(request: Request):
    return templates.TemplateResponse("texts_upload.html", {'request': request, 'texts': List[Text]})

@router_texts.get('/{id}')
async def get_text_info(id: int, request: Request):
    return templates.TemplateResponse("text_info.html", {'request': request, 'texts': Text})