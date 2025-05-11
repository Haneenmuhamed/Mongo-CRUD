from pydantic import BaseModel, validator



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
