from fastapi import APIRouter, Body ,Query
from models.item_model import Item
from services.user_service import insert_item, retrieve_item, update_item, delete, search

router = APIRouter()

@router.post("/add")
def create(item: Item):
    return insert_item(item.model_dump())

@router.get("/get/{name}")
def get_item(name:str):
    return retrieve_item(name)

@router.put("/update/{name}")
def update(name:str,item:Item = Body(...)):
    return update_item(name, item.model_dump())

@router.delete("/delete/{name}")
def delete_item(name:str):
    return delete(name)
@router.get("/search")
def search_item(q:str =Query(min_length=1,description="Search keyword must not be empty")):
    return search(q)