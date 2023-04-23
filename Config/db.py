from pymongo import MongoClient

uri = "mongodb+srv://SteelEye:SteelEye1@cluster0.zvrnutx.mongodb.net/STEELEYEASSIGNMENT?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client["STEELEYEASSIGNMENT"]

trades_collection = db["trades"]

def get_all_trades():
    trades = []
    for trade in trades_collection.find():
        trades.append(trade)
    return trades