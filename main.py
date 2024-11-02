from fastapi import FastAPI
from parsers.maxidom import get_products_roof

app = FastAPI()


@app.get("/")
async def get_products():
    return get_products_roof()
