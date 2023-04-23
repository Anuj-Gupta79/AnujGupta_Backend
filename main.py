from fastapi import FastAPI
from Routers.Trade import trade


app = FastAPI()

@app.get('/')
async def main():
    return {"message" : "This is SteelEye Assignment!"}

app.include_router(trade)