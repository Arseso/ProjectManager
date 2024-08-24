import asyncpg
from src.web import config

async def connection() -> asyncpg.connection:
    connection = await asyncpg.connect(host= config.DB_HOST,
                             port=config.DB_PORT,
                             user=config.DB_USER,
                             password=config.DB_PASS,
                             database=config.DB_NAME)