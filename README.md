# buysellbot
derebit bot for sell or buy eth or btc perpetual ,separate big size for any small value
work with cctx library
on the console
this use for buy and sell for bid or asc price or with price correction cheaper for sell and highter for buy.

to run you need either ccxt
to install it, you need to type pip install ccxt at the command line

need to replace

deribit = ccxt.deribit({
'apiKey': 'xxx',
'secret': 'xxx',
})
  xxx to your api keys
deribit.set_sandbox_mode(True) this line means that the launch will be on
test.derebit.com

if you will run on a working account, replace the keys with those from it and delete
or comment out this line deribit.set_sandbox_mode(True)
