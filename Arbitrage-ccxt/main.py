# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:44:02 2018



"""



import ccxt
import time

def calc():
    """
    Bitfinex 
    
    bitfinex = ccxt.bitfinex()
    markets = bitfinex.load_markets ()
    
    orderbook = bitfinex.fetch_order_book ('BTC/USD')
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    spread = (ask - bid) if (bid and ask) else None
    print (bitfinex.id, 'market price', { 'bid': bid, 'ask': ask, 'spread': spread })
    
    
    Cex.io 
     
    
    cex = ccxt.cex()
    
    orderbook = cex.fetch_order_book ('BTC/USD')
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    spread = (ask - bid) if (bid and ask) else None
    print (cex.id, 'market price', { 'bid': bid, 'ask': ask, 'spread': spread })
    """
    
    bitfinex = ccxt.bitfinex()
    cex = ccxt.cex()
    kucoin = ccxt.kucoin()
    poloniex=ccxt.poloniex()
    bittrex=ccxt.bittrex()
    
    
    FEE = 1.02 # fee for every trade (2%)
    Diff = 0.5 # 1 % arbitrage to execute
    curr = ["NEO/BTC", "ETH/BTC", "LTC/BTC", "OMG/BTC", "QTUM/BTC", "XEM/BTC"] #currencies to trade if arbitrage is found
    exc = [bitfinex, cex, kucoin, poloniex, bittrex] #exchanges to trade on for the function calls
    
    
    
    
    
    def getAsk(market, sym):
        orderbook = market.fetch_order_book(sym)
        ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
        return ask
    
    def getBid(market, sym):
        orderbook = market.fetch_order_book(sym)
        bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
        return bid  
     
    
    aa = getAsk(exc[0], curr[0])
    bb = getBid(cex, 'BTC/USD')
    
    #print ('cex BTC/USD ask:', aa, 'Cex bid', bb)
    
    
    def compare():
    	print ("Arbitrage Trader starting up...")
    	pairpart2 = "btc"
    
    	n=0
    	while n<=(len(curr)-1):
    		print ("Starting Arbitrage checking for ", curr[n])
    		pairpart1 = curr[n]
    		m=0
    		while m<=(len(exc)-1):
    			#print "m = " + str(m)
    			k = 0
    			while k<=(len(exc)-1):
    				#print "k = " + str(k)
    				try:
    					sprice = getBid(exc[m], curr[n])
    					bprice = getAsk(exc[k], curr[n])
    					
    				except Exception:
    					pass
    
    				#print ("Sell price = " , str(sprice) , " on " , exc[m])
    				#print ("Buy price  = " , str(bprice) , " on " , exc[k])
    				
    				if (float(bprice) < float(sprice)):
    					#print ("Opportunity to buy " , curr[n] , " for ", str(bprice), " on ",exc[k]," and sell for " , str(sprice) , " on " , exc[m])
    					yie = ((float(sprice) - float(bprice))/float(sprice))*100.0;
    					#print ("Yield before trading costs would be: ",str(yie),"%")
    					
    				if (((float(sprice) - float(bprice))/float(sprice))*100.0 > Diff):
    					# make_trade(exc[m], "buy", amount1, pairpart1, "btc", bprice)
                        # make_trade(exc[k], "sell", amount1, pairpart1, "btc", sprice)
                        #printouts for debugging
    					print ("price on " , exc[m].id , " for " , curr[n] , " is " , str(sprice) , " BTC")
    					print ("price on " , exc[k].id , " for " , curr[n] , " is " , str(bprice) , " BTC")
    					print ("executing trade at a win per 1" , curr[n] , " of " , str(round(((sprice * FEE)-(bprice * Diff * FEE)),8)) , "BTC")
    					print ("net kar" , str(round(100*((sprice * 0.998)-(bprice * 1.002))/(sprice * 0.998),8)))
    				else:
    					try:
    						sprice = getBid(exc[k], curr[n])
    						bprice = getAsk(exc[m], curr[n])
    					except Exception:
    						pass
    					if (((float(sprice) - float(bprice))/float(sprice))*100.0 > Diff):
    						# make_trade(exc[k], "buy", amount1, pairpart1, "btc", bprice)
    						# make_trade(exc[m], "sell", amount1, pairpart1, "btc", sprice)
    						#printouts for debugging
    						print ("price on " , exc[k].id , " for " , curr[n] , " is " , str(sprice) , " BTC")
    						print ("price on " , exc[m].id , " for " , curr[n] , " is " , str(bprice) , " BTC")
    						print ("executing trade at a win per 1" , curr[n] , " of " , str(round(((sprice * FEE)-(bprice * Diff * FEE)),8)) , "BTC")
    						print ("net kar" , str(round(100*((sprice * 0.998)-(bprice * 1.002))/(sprice * 0.998),8)))
    				k+=1
    			m+=1
    		n+=1





    compare()



calc()


"""
def my_timer(*args):
    calc()
    return True# do ur work here, but not for long

gtk.timeout_add(60*1000, my_timer) # call every min
"""


"""
delay =2
for symbol in bitfinex.markets:
    print (bitfinex.fetch_order_book ('BTC/USD'))
    time.sleep (delay) # rate limit
    
"""

"""

# any time
bitfinex = ccxt.bitfinex ()
bitfinex.apiKey = 'YOUR_BFX_API_KEY'
bitfinex.secret = 'YOUR_BFX_SECRET'

# upon instantiation
hitbtc = ccxt.hitbtc ({
    'apiKey': 'YOUR_HITBTC_API_KEY',
    'secret': 'YOUR_HITBTC_SECRET_KEY',
})

"""