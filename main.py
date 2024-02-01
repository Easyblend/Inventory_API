from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()


class Products(BaseModel):
    id: int
    name:str
    price:float
    brand:str

item = [{
            "id": 1,
            "name": "Lubricant",
            "price": 32.0,
            "brand": "Wax"
        },
        {
            "id": 2,
            "name": "condoms",
            "price": 12.0,
            "brand": "Kiss"
        },
        {
            "id": 3,
            "name": "Milk",
            "price": 7.0,
            "brand": "Ideal"
        }]    

#write a function to loop through my dict of items and return the one with the id equal to the parameter
def updateProduct(id, item:Products):
    for i,p in enumerate(item):
        if item[i]["id"] == id:
            return p
    return {"data":"not found"}


@app.get("/")
def root():
    return {"data":item}


@app.post("/add")
def add(items: Products):
    item.append(items.dict())
    return {"data":items}


@app.put("/update/{id}")
def update(id:int, payload:Products):
    newItem = updateProduct(id, item)
    if newItem is not None:
        item[id-1] = payload.dict()
        return {"data":payload}
    return {"data":"not found"}


@app.delete("/delete/{id}")
def delete(id:int):
    item.pop(id-1)
    return {"data":item}