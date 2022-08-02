from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class esp(BaseModel):
    id: int
    state: bool
    timerval: int
    timerstate: bool


app = FastAPI()

device = {"id":[0],"state":[0], "timerval":[0], "timerstate":[0]};

@app.post("/")
async def create_item(item: esp):
    device["id"].append(item.id)
    device["state"].append(item.state)
    device["timerval"].append(item.timerval)
    device["timerstate"].append(item.timerstate)
    return {"Status": "Send Successfully"}


@app.post("/switch")
async def create_item(item: esp):
    python_indices  = [index for (index, items) in enumerate(device["id"]) if items == item.id]
    return {"id": device["id"][python_indices[-1]], "switchstate": device["state"][python_indices[-1]], "timerval": device["timerval"][python_indices[-1]], "timerstate": device["timerstate"][python_indices[-1]]}

#{
#    "id" : 123,
#    "switchstate": bool,
#    "timerval": int,
#    "timerstate": bool
#}