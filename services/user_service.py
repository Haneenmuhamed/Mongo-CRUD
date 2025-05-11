from db.user_repository import insert , get_one_by_name ,update_item_by_name , delete_item , search_item
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

def update_item(name:str, updated_data:dict):
    existing_user =get_one_by_name(name)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"message":"Item not Found"})
    success= update_item_by_name(name, updated_data)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="update failed")
    return {"message":"Item Updated Successfully"}

def delete(name:str):
    existing_user=get_one_by_name(name)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="user not found")
    delete_item(name)
    return  {"message":"Item Deleted Successfully"}

def search(keyword :str):
    result=search_item(keyword)
    clean_results=[]
    for doc in result :
         doc["_id"]= str(doc["_id"])
         clean_results.append(doc)
    return  clean_results

