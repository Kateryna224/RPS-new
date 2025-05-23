
from fastapi import APIRouter, HTTPException
from app.models.item import Item
from app.crud import items

router = APIRouter()

@router.post("/items/")
def create_item(item_id: int, item: Item):
    return items.create_item(item_id, item.dict())

@router.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.read_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/items/")
def get_items():
    return items.read_items()

@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    updated = items.update_item(item_id, item.dict())
    if updated is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    deleted = items.delete_item(item_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"ok": True}
