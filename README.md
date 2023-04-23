## Table of contents
1. [Overview](#Overview)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)


### Overview:
Here, We have build an app using the framework of python i.e. FastApi. The task has given to us. We have given a mock database schema name as 'Trade'. We need to create a mock database server and insert some mock data of 'Trade'.

***
 We need to create a endpoint -
->  to fetch all the trades.
-> to fetch a trade using the trade_id in path parameter.
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
***

   
#First Step:-
 We create main.py file and install fastapi and uvicorn for building endpoint and start the server.
 ```bash
pip install foobar
```
 ○ pip install uvicorn
 Then , We create the app and just start the server by writing this command.
 ○ uvicorn main:app --reload
 main is file name of main file i.e. main.py and app is the that we have created and --reload is to start the server  and reload automatically after certain changes in our code.

 
<!--  ## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
5. [FAQs](#faqs)
### General Info
***
Write down general information about your project. It is a good idea to always put a project status in the readme file. This is where you can add it. 
### Screenshot
![Image text](https://www.united-internet.de/fileadmin/user_upload/Brands/Downloads/Logo_IONOS_by.jpg)
## Technologies
***
A list of technologies used within the project:
* [Technology name](https://example.com): Version 12.3 
* [Technology name](https://example.com): Version 2.34
* [Library name](https://example.com): Version 1234
## Installation
***
A little intro about the installation. 
```
$ git clone https://example.com
$ cd ../path/to/the/file
$ npm install
$ npm start
```
Side information: To use the application in a special environment use ```lorem ipsum``` to start
## Collaboration
***
Give instructions on how to collaborate with your project.
> Maybe you want to write a quote in this part. 
> Should it encompass several lines?
> This is how you do it.
## FAQs
***
A list of frequently asked questions
1. **This is a question in bold**
Answer to the first question with _italic words_. 
2. __Second question in bold__ 
To answer this question, we use an unordered list:
* First point
* Second Point
* Third point
3. **Third question in bold**
Answer to the third question with *italic words*.
4. **Fourth question in bold**
| Headline 1 in the tablehead | Headline 2 in the tablehead | Headline 3 in the tablehead |
|:--------------|:-------------:|--------------:|
| text-align left | text-align center | text-align right |
 -->
