from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from .exceptions import ItemNotFound, ItemAlredyExists
from .users.router import users
from .cars.router import cars, manufacturers


app = FastAPI(
    title='Car Web Service'
)


@app.exception_handler(ItemNotFound)
async def on_not_found(request: Request, exc: ItemNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={'detail': 'item not found' if len(exc.args) == 0 else exc.args[0]}
    )


@app.exception_handler(ItemAlredyExists)
async def on_alerady_exists(request: Request, exc: ItemAlredyExists):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'detail': 'item already exists' if len(exc.args) == 0 else exc.args[0]}
    )


app.include_router(users)
app.include_router(cars)
app.include_router(manufacturers)
