
from fastapi import APIRouter
from .endpoints import healthz_router

main_router = APIRouter()

main_router.include_router(
    healthz_router,
    prefix="/status",
    tags=["K8s health check"],

)
