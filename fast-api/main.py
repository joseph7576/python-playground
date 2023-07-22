# from: https://www.youtube.com/watch?v=tLKKmouUams
# and: https://fastapi.tiangolo.com/tutorial/ -> mostly - so cool doc man :D
#? install it using pip install "fastapi[all]"
#! also check python types intro from this official docs :D
#* this is just for testing and learning - not the actual software


from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



app = FastAPI()


@app.get("/") # A "path" is also commonly called an "endpoint" or a "route".
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}") # path parameter
async def read_item_first(item_id:int): # declare types
    return {"item_id": item_id}

# parsing: convert string from http request to python data 

# the order matters in urls 
@app.get("/users/me") # this should come before the path below
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}") # path matches the first thing it find
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: # Compare enumeration members
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet": # Get the enumeration value #? model_name.lenet.value
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

#? When you declare other function parameters that are not part of the path parameters, 
#? they are automatically interpreted as "query" parameters.

# for python 3.6+ the line 62 would be 'Union[str, None]' imported from typing module for the pipe '|' part
# all the example with | also holds true :(
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None): # q is query parameter, item_id is the path parameter
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item_first(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#? If you don't want to add a specific value but just make it optional, set the default as None.

''' The path operation function below will have 3 query parameters:

- needy, a required str.
- skip, an int with a default value of 0.
- limit, an optional int.
'''
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None # i'm using python 3.10+ :D
    price: float
    tax: float | None = None
    

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump() # dict() is deprecated
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


from typing import Annotated
from fastapi import FastAPI, Query, Path


# async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
# ... means it's required! #? https://docs.python.org/3/library/constants.html#Ellipsis
# add more meta data to this :D
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#         ),
#     ] = None
# ):
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None): 
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q}) # type: ignore
    return results


@app.get("/items/{item_id}")
async def read_items_pro(
    item_id: Annotated[int, Path(title="The ID of the item to get")], # add more metadata to path parameter
    q: Annotated[str | None, Query(alias="item-query")] = None, # and we have some query parameters too :D
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q}) # type: ignore
    return results


@app.get("/items/{item_id}")
async def read_items_more_pro(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)], # more validation
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q}) # type: ignore
    return results