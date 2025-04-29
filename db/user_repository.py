from db_crud import collection



def insert(data:dict):
    collection.insert_one(data)


def get_one_by_name(name: str):
    doc = collection.find_one({"name": name})
    if doc :
        doc.pop("_id",None)
    return doc
