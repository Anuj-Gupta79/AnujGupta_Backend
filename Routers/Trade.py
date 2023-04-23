from fastapi import APIRouter, Query
from Model.Trade import Trade
from Config.db import trades_collection
import datetime as dt
from typing import Optional


trade = APIRouter()

#Pagination and Sorting has been done
#Getting all the trade based on certain condition like counterparty, instrumentId, instrumentName, trader
#If there is no search parameter then it gives us all the trades from our database.
@trade.get('/trades')
async def get_trades(search: str = Query(default=None),page : int = 1, per_page : int = 10, sort: str = Query(None, max_length=50)):
    beg = (page - 1)*per_page
    last = beg + per_page
    all_trades = []
    if search:
        all_trades = [trade for trade in trades_collection.find() if search.lower() in str(trade).lower()]
    else:
        all_trades = list(trades_collection.find())
    
   
    for trade in all_trades:
        trade['_id'] = str(trade['_id'])
    
    
    if len(all_trades):
        if sort:
            sorted_trades = sorted(all_trades, key=lambda x: x[sort])
            return sorted_trades[beg : last]
        return all_trades[beg : last]
    
    return {"message": "Trades not found"}
    
# get trade by tradeId
@trade.get("/trades/{trade_id}")
async def get_trade(trade_id: str):
    all_trades = list(trades_collection.find())
    
    for trade in all_trades:
        if trade['trade_id']==trade_id:
            trade['_id'] = str(trade['_id'])
            return trade
    
    return {"message": "Trade not found"}

#Pagination and Sorting has been done.
#get trade by advanced filtering
@trade.get('/advancedFiltering/trades')
async def filter_trades(asset_class: str = None, end: dt.datetime = None, max_price: float = None, min_price: float = None, start: dt.datetime = None, trade_type: str = None, page : int = 1, per_page : int = 10, sort: str = Query(None, max_length=50)):
    beg = (page - 1)*per_page
    last = beg + per_page
    filtered_trades = list(trades_collection.find());
    if asset_class:
        filtered_trades = [trade for trade in trades_collection.find() if asset_class.lower() in str(trade).lower()]
    if end:
        filtered_trades = [
            trade for trade in filtered_trades if trade['trade_date_time'] <= end]
    if max_price:
        filtered_trades = [
            trade for trade in filtered_trades if trade['trade_details']['price'] <= max_price]
    if min_price:
        filtered_trades = [
            trade for trade in filtered_trades if trade['trade_details']['price'] >= min_price]
    if start:
        filtered_trades = [
            trade for trade in filtered_trades if trade['trade_date_time'] >= start]
    if trade_type:
        filtered_trades = [
            trade for trade in filtered_trades if trade['trade_details']['buySellIndicator'] == trade_type]
    
    for trade in filtered_trades:
        trade['_id'] = str(trade['_id'])
    
    if len(filtered_trades):
        if sort:
            sorted_trades = sorted(filtered_trades, key=lambda x: x[sort])
            return sorted_trades[beg : last]
        return filtered_trades[beg : last]
    
    return {"message" : "Trades not found"}


#Inserting the trade to our database
@trade.post('/trades/insert')
async def insert_trade(trade : Trade):
    trade_dic = trade.dict()
    trades_collection.insert_one(trade_dic)
    return {"message" : "trade insert successfully!"}