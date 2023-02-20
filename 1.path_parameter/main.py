from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


profile = [{"beth": {"name": "elizabeth jane yaginuma", "age": 28}}]

beth = profile[0]

@app.get("/aboutbeth/")
async def profile_beth():
    return beth["beth"]


@app.get("/aboutbeth/{attr}")
async def profile_beth(attr: str):
    return {"name": item_id}


from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}