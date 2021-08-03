def zip_dict(a, b):
    b = dict(zip(a, b))
    print(b)


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
zip_dict(coin, code)
