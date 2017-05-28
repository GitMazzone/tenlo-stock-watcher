# Tenlo Stock Watcher  
###### Based on the method described by [theBrokeQuant](http://thebrokequant.blogspot.com/).  
  
### Basic functionality:  
Buy stock **if**:  
* Stock is above 50 day [moving average](http://www.investopedia.com/terms/m/movingaverage.asp)  
* **AND** stock is above 100 day moving average  
* **AND** stock hits a new 10 day low  

Sell stock **if**:  
* Stock hits a new 10 day high
* **OR** price drops below 50 day moving average
* **OR** price drops below the [stop loss](http://www.investopedia.com/terms/s/stop-lossorder.asp)  
* **OR** have been holding the [security](http://www.investopedia.com/terms/s/security.asp) for 10 days  
  
### Usage Instructions:  
(will be updated when functionality is added)
### Technologies used:
* [Intrinio Web API](https://intrinio.com/sdk/web-api) - provides info like current and historical price, company info, and more  
* [Matplotlib](https://matplotlib.org/) - for graphing financial histories and other data  
* [Python 3.xx](https://www.python.org/downloads/)
  
##### Note:  
This is an ongoing side project intended to be a learning experience in Python, finance, and data science. All work is published under the MIT License. 
