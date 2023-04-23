# Table of contents
1. [Overview](#Overview)
2. [Installation](#Installation)
3. [Files And Folder](#Files-And-Folder)
4. [Endpoints](#Enpoints)
5. [Outputs](#Outputs)


## Overview:
Here, We have build an app using the framework of python i.e. FastApi. The task has given to us. We have given a mock database schema name as 'Trade'. We need to create a mock database server and insert some mock data of 'Trade'.

***
 We need to create following endpoints :-
 1. To fetch all the trades.
 
 2. To fetch a trade using the trade_id in path parameter.
 
 3. To fetch all the trades on the basis of certain conditions like:-
   * counterparty :- Couter party of the trade.
   * instrumentId :- Instrument Id of the tarde.
   * instrumentName :- Instrument Name of the trade.
   * trader :- Trader Name of the trade.```
   
 4. To fetch all the trades on the basis of advanced filtering i.e :-
 
   * assetClass :- Asset class of the trade.
   * end :- The maximum date for the tradeDateTime field.
   * maxPrice :- The maximum value for the tradeDetails.price field.
   * minPrice :-	The minimum value for the tradeDetails.price field.
   * start	The minimum date for the tradeDateTime field.
   * tradeType	The tradeDetails.buySellIndicator is a BUY or SELL.
***
**Note :- We have also done pagination and sorting.**  

## Installation:
* Install fastapi and uvicorn to build endpoint and start the server.
 ```bash
pip install fastapi
```
```bash
pip install uvicorn
```
* Create main.py and make an app and write the command to run the server.Server is running on http://localhost:8000
```bash
uvicorn main:app --reload
 ```
* Set up a mock database on mongdb atlas and then make db.py and insall the mongodb. Connect the mongodb through the url.
```bash
python -m pip install pymongo
```
## Files And Folder:
1. main.py :- Set up of the server.
2. Config->db.py :- Set up the mongodb database.
3. Model->Trade.py :- Write the schema for the trade.
4. Model->TradeDetails.py :- Write the schema for the trade details.
5. Routers->Trade.py :- Creating the router for the end points.

## Endpoints:
1. To fetch allll the tardes:-
   >Get Request :- This end will fetech all the trade. 
   ```http://localhost:8000/trades```
3. To fetch 

 

