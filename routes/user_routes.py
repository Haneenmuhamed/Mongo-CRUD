from fastapi import APIRouter
from models.item_model import Item
from services.user_service import insert_item, retrieve_item


router = APIRouter()

@router.post("/add")
def create(item: Item):
    return insert_item(item.model_dump())

@router.get("/get/{name}")
def get_item(name:str):
    return retrieve_item(name)
