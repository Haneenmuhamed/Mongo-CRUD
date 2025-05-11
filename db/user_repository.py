from db_crud import collection



def insert(data:dict):
    collection.insert_one(data)


def get_one_by_name(name: str):
    doc = collection.find_one({"name": name})
    if doc :
        doc.pop("_id",None)
    return doc


def update_item_by_name(name:str ,updated_data:dict):
    return collection.update_one({"name":name},{"$set":updated_data})


def delete_item(name:str):
    return collection.delete_one({"name":name})

def search_item(keyword: str):
    return list(collection.find({"$text":{"$search":keyword}}))
