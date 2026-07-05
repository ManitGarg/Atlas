from fastapi import APIRouter
from app.api.routes.health import router as health_router
from app.api.routes.user import router as user_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(user_router)