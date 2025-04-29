from db.user_repository import insert , get_one_by_name
from fastapi import HTTPException , status


def insert_item(data: dict):
    existing_user = get_one_by_name(data["name"])
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User already Exists")
    insert(data)
    return {"message":"Data inserted successfully "}

def retrieve_item(name:str):
    item = get_one_by_name(name)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"message":"Item not found"})
    return item