## AnujGupta_Backend

# Overview:
Here, We have build an app using the framework of python i.e. FastApi. The task has given to us. We have given a mock database schema name as 'Trade'. We need to create a mock database server and insert some mock data of 'Trade'.

# We need to create a endpoint -
  # to fetch all the trades.
  # to fetch a trade using the trade_id in path parameter.
-> to fetch all the trades on the basis of certain conditions like:-
   • counterparty :- Couter party of the trade.
   • instrumentId :- Instrument Id of the tarde.
   • instrumentName :- Instrument Name of the trade.
   • trader :- Trader Name of the trade.
-> to fetch all the trades on the basis of advanced filtering i.e :-
   • assetClass :- Asset class of the trade.
   • end :- The maximum date for the tradeDateTime field.
   • maxPrice :- The maximum value for the tradeDetails.price field.
   • minPrice :-	The minimum value for the tradeDetails.price field.
   • start	The minimum date for the tradeDateTime field.
   • tradeType	The tradeDetails.buySellIndicator is a BUY or SELL.
   
#First Step:-
 We create main.py file and install fastapi and uvicorn for building endpoint and start the server.
 ○ pip install fastapi
 ○ pip install uvicorn
 Then , We create the app and just start the server by writing this command.
 ○ uvicorn main:app --reload
 main is file name of main file i.e. main.py and app is the that we have created and --reload is to start the server  and reload automatically after certain changes in our code.
