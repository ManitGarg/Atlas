from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine
from sqlalchemy import text

app = FastAPI(
    title="Atlas API",
    description="Backend API for Atlas - Personal Student Operating System",
    version="1.0.0"
)

@app.get("/")
def root():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        db_version = result.scalar()

    return {
        "app": settings.APP_NAME,
        "database": "Connected Successfully ✅",
        "postgres_version": db_version
    }