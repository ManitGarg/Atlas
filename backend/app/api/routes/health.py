from fastapi import APIRouter
from sqlalchemy import text

from app.core.config import settings
from app.db.session import engine

router = APIRouter()


@router.get("/")
def health_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        db_version = result.scalar()

    return {
        "app": settings.APP_NAME,
        "database": "Connected Successfully ✅",
        "postgres_version": db_version,
    }