from src.fsdc_calories.src
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/charts/price_ranking")
async def price_charts():
    DataCal().gen_graphs().to_html()
