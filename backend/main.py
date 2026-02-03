from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

items = {}

class Item(BaseModel):
    name: str
    description: Optional[str] = None

@app.get("/items", response_model = List[Item])
def read_items():
  return list(items.values())

@app.post("/items")
def create_item(item: Item):
  if item.name in items:
    raise HTTPException(status_code = 400, detail = "Item already exists")
  items[item.name] = item
  return item

@app.delete("/items/{name}")
def delete_item(name: str):
  if name not in items:
    raise HTTPException(status_code = 404, detail = "Item not found")
  del items[name]
  return {"message": "Deleted successfully"}
