from http.client import HTTPException

from fastapi import FastAPI ,HTTPException , status
from pydantic import BaseModel, validator
from db_crud import insert, get_one_by_name

app = FastAPI()

# Pydantic model for input validation
class Item(BaseModel):
    name: str
    age: int
    address : str
    job : str

    @validator('age')
    def check_age_not_zero(cls, v):
        if v == 0:
            raise ValueError('Age cannot be zero')
        return v
    @validator('name')
    def check_name_not_empty(cls, v):
        if not v.strip():  # Strip is used to ensure no whitespace-only names
            raise ValueError('Name cannot be empty')
        return v
    @validator('address')
    def check_address_not_empty(cls, v):
        if not v.strip():  # Strip is used to ensure no whitespace-only names
            raise ValueError('address cannot be empty')
        return v

@app.post("/add")
def create(item: Item):
    return insert(item.dict())

@app.get("/get/{name}")
def get_item(name:str):
    result=get_one_by_name(name)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with name'{name}'not found"
                            )
    return result
