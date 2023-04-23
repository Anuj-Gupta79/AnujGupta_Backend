## Table of contents
1. [Overview](#Overview)
2. [Installation](#Installation)
3. [Files And Folder](#Files-And-Folder)
4. [Endpoints And Output](#Enpoints-And-Output)


### Overview:
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
**Note :- We have also done pagination and sorting.  

### Installation:
* Install fastapi and uvicorn to build endpoint and start the server.
 ```bash
pip install fastapi
```
```bash
pip install uvicorn
```
* Create main.py and make an app and write the command to run the server.
```bash
uvicorn main:app --reload
 ```
* Set up a mock database on mongdb atlas and then make db.py and insall the mongodb. Connect the mongodb through the url.
```bash
python -m pip install pymongo
```
### Files And Folder:
**main.py :- Set up of the server.**


 
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
