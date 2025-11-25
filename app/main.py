from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from psychic_calculator import add, subtract, multiply, divide


class Operands(BaseModel):
    a: float
    b: float


app = FastAPI(title="Psychic Calculator API")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/add")
def api_add(payload: Operands) -> dict:
    return {"result": add(payload.a, payload.b)}


@app.post("/subtract")
def api_subtract(payload: Operands) -> dict:
    return {"result": subtract(payload.a, payload.b)}


@app.post("/multiply")
def api_multiply(payload: Operands) -> dict:
    return {"result": multiply(payload.a, payload.b)}


@app.post("/divide")
def api_divide(payload: Operands) -> dict:
    try:
        return {"result": divide(payload.a, payload.b)}
    except ZeroDivisionError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
