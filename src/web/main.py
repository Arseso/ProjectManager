from fastapi import FastAPI
from web.routers.operations import router as operation_router
from web.routers.pages import router as pages_router
app = FastAPI("Cover letter analyzer")

app.include_router(operation_router)
app.include_router(pages_router)