from fastapi import FastAPI

from app.api.router import api_router
from app.db.init_db import init_db

app = FastAPI(
    title="Atlas API",
    description="Backend API for Atlas - Personal Student Operating System",
    version="1.0.0",
)


@app.on_event("startup")
def startup():
    print("🚀 Starting Atlas API...")
    init_db()


app.include_router(api_router)