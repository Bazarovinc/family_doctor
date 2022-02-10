from fastapi import APIRouter

from weather.api import router


def include_routers():
    main_router = APIRouter()
    main_router.include_router(router, prefix='/weather')
    return main_router
