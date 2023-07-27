import ccxt
import time

deribit = ccxt.deribit({
'apiKey': 'xxx',
'secret': 'xxx',
})

deribit.set_sandbox_mode(True)

print('Please enter : asset,order amount,type of deal sell or buy,size in order book,advantage in order size ')
print('example : eth 10 buy 1000 1')
user_input= input()
user_input_list=user_input.split(' ')

if user_input_list[0] ==  'eth' :
    asset='ETH-PERPETUAL'
elif user_input_list[0] == 'btc' :
    asset='BTC-PERPETUAL'
else :
    print('unknow asset')
order_type=user_input_list[2]
order_size=float(user_input_list[3])
order_amount=int(user_input_list[1])
order_adv=float(user_input_list[4])



for i in range(1,order_amount + 1) :

    if asset == 'ETH-PERPETUAL' and order_type == 'buy':
        eth_ticker = deribit.fetch_ticker('ETH-PERPETUAL')
        order = deribit.create_order(asset, 'limit', order_type, order_size, eth_ticker['bid'])
    elif asset == 'BTC-PERPETUAL' and order_type == 'buy':
        btc_ticker = deribit.fetch_ticker('BTC-PERPETUAL')
        order = deribit.create_order(asset, 'limit', order_type, order_size, btc_ticker['bid'])
    elif asset == 'ETH-PERPETUAL' and order_type == 'sell':
        eth_ticker = deribit.fetch_ticker('ETH-PERPETUAL')
        order = deribit.create_order(asset, 'limit', order_type, order_size, eth_ticker['ask'])
    elif asset == 'BTC-PERPETUAL' and order_type == 'sell':
        btc_ticker = deribit.fetch_ticker('BTC-PERPETUAL')
        order = deribit.create_order(asset, 'limit', order_type, order_size, btc_ticker['ask'])

   
    while True:
        time.sleep(1)
        eth_position=deribit.fetchPosition('ETH-PERPETUAL')
        btc_position=deribit.fetchPosition('BTC-PERPETUAL')
        if asset == 'ETH-PERPETUAL' and order_type == 'buy' :
            eth_ticker = deribit.fetch_ticker('ETH-PERPETUAL')
            try:
                editorder = deribit.editOrder(order['id'],asset, 'limit', order_type, order_size, eth_ticker['bid']+order_adv)
            except Exception as err:
                break
        elif asset == 'BTC-PERPETUAL' and order_type == 'buy' :
            btc_ticker = deribit.fetch_ticker('BTC-PERPETUAL')
            try:
                editorder = deribit.editOrder(order['id'],asset, 'limit', order_type, order_size, btc_ticker['bid']+order_adv)
            except Exception as err:
                break
        if asset == 'ETH-PERPETUAL' and order_type == 'sell' :
            eth_ticker = deribit.fetch_ticker('ETH-PERPETUAL')
            try:
                editorder = deribit.editOrder(order['id'],asset, 'limit', order_type, order_size, eth_ticker['ask']-order_adv)
            except Exception as err:
                break
        elif asset == 'BTC-PERPETUAL' and order_type == 'sell' :
            btc_ticker = deribit.fetch_ticker('BTC-PERPETUAL')
            try:
                editorder = deribit.editOrder(order['id'],asset, 'limit', order_type, order_size, btc_ticker['ask']-order_adv)
            except Exception as err:
                break
