# from: https://www.youtube.com/watch?v=tLKKmouUams
# and: https://fastapi.tiangolo.com/tutorial/ -> mostly - so cool doc man :D
#? install it using pip install "fastapi[all]"


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