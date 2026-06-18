from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException,
):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": f"Route '{request.url.path}' not found",
            },
        )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
        },
    )