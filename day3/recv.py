from typing import Any, Dict

from fastapi import FastAPI
from rich.pretty import pprint

app = FastAPI()


@app.post("/")
def recv_webhook(payload: Dict[Any, Any]):
    pprint(payload)

