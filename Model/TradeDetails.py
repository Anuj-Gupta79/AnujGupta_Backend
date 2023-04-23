from pydantic import BaseModel, Field

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(
        description="A value of BUY for buys, SELL for sells.")
    price: float = Field(description="The price of the Trade.")
    quantity: int = Field(description="The amount of units traded.")