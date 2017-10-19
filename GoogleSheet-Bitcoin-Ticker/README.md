# Google Sheets Bitfinex Ticker
Simple code takes last price of currencies from Bitfinex.

## Installation
- Just copy the code in GoogleSheetBitcoinTicker.js and paste it to <i>Tools > Script Editor</i> in Google Sheet. 
- Save project as "Bitfinex" name and close Script Editor.

## Calling Bitfinex function
In Sheet just type <code> =Bitfinex("ETHBTC") </code> for ETH/BTC price for example. (it works every currency in Bitfinex)<br> 
For auto refresh type <code>=Bitfinex("ETHBTC"; Z1)</code> when you change any cell in the sheet, price will be reloaded.*
<br><br>
*Google does not allow auto refresh for custom functions (or just i don't know how it's done). So Z1 parameter is just for cheating Google Sheet. When edited any cell in sheet, code put a random number in Z1 cell. So when Z1 is given as a parameter to Bitfinex function, price is reloaded. <br>Yeah, it's maybe looks stupid but never forget: If it's stupid and it works, it ain't stupid.
