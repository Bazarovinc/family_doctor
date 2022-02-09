from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from core.database import database
from core.exceptions.base_http_exception import BaseHTTPException
from core.routers import include_routers


def create_app() -> FastAPI:
    from core.containers.base_container import Container

    app = FastAPI()
    database.setup_database(app)
    app.include_router(include_routers(), prefix='/api')
    container = Container()
    app.container = container
    return app


app = create_app()
# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0", port=8000)


@app.exception_handler(BaseHTTPException)
async def unicorn_exception_handler(request: Request, exc: BaseHTTPException):
    return JSONResponse(
        status_code=exc.status,
        content={"message": exc.message},
    )
