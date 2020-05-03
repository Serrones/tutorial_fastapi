from fastapi import FastAPI

from enums import ItemOption

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item}")
async def read_item(item: ItemOption):
    if item == ItemOption.office:
        return {"item": item, 'message': 'items for office'}
    if item == ItemOption.home:
        return {"item": item, 'message': 'items for home'}
    return {"item": item, 'message': 'items for travel'}
