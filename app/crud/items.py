
items_db = {}

def create_item(item_id: int, item: dict):
    items_db[item_id] = item
    return item

def read_item(item_id: int):
    return items_db.get(item_id)

def read_items():
    return items_db

def update_item(item_id: int, item: dict):
    if item_id in items_db:
        items_db[item_id] = item
        return item
    return None

def delete_item(item_id: int):
    return items_db.pop(item_id, None)
