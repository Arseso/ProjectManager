from typing import List
from fastapi import APIRouter, File, UploadFile
from src.web.models import Text
router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)

@router.get('/search/{search_request}')
async def search(search_request: str):
    # Search by request 
    raise NotImplementedError
    
@router.post('/submit')
async def upload_texts(files: List[UploadFile] = File(...)):
    file_contents = []
    for file in files:
        content = await file.read()  # Чтение содержимого файла
        file_contents.append({
            "filename": file.filename,
            "content": content.decode("utf-8")  # Декодируем содержимое в строку
        })
    # Логика обработки файлов может быть добавлена здесь.
    return {"files": file_contents}


@router.get('/texts')
async def get_texts() -> List[Text]:
    raise NotImplementedError

@router.get('/texts/{id}')
async def get_text_info(id: int) -> Text:
    raise NotImplementedError