"""
App's main script, which contains all path methods
"""

from fastapi import FastAPI

from enums import ItemOption

app = FastAPI()


@app.get("/")
async def root():
    """
    Root path. A simple hello world
    """
    return {"message": "Hello World"}


@app.get("/items/{item}")
async def read_item(item: ItemOption):
    """
    GET method with path parameter
    """
    if item == ItemOption.office:
        return {"item": item, 'message': 'items for office'}
    if item == ItemOption.home:
        return {"item": item, 'message': 'items for home'}
    return {"item": item, 'message': 'items for travel'}
