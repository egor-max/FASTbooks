from fastapi import (
    APIRouter,
    status,
)
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/healthz")

async def healthz() -> JSONResponse:
    """_summary_

    Returns:
        JSONResponse: _description_
    """
    
    return JSONResponse(content={"OK": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)
