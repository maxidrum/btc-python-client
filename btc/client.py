import requests

BASE_URL = "https://btc-trade.com.ua/api/"


class Client(object):
    def __init__(self):
        pass

    def get_deals(self, pair):
        url = BASE_URL + 'deals/{0}'.format(pair)
        response = requests.get(url)
        return response.json()

    def get_trades_sell(self, pair):
        url = BASE_URL + 'trades/sell/{0}'.format(pair)
        response = requests.get(url)
        return response.json()

    def get_trades_buy(self, pair):
        url = BASE_URL + 'trades/buy/{0}'.format(pair)
        response = requests.get(url)
        return response.json()

    def get_japan_stat(self, pair):
        url = BASE_URL + 'japan_stat/high/{0}'.format(pair)
        response = requests.get(url)
        return response.json()

    def auth_request(self):
        pass

    def get_balance(self):
        pass

    def bid_sell(self):
        pass

    def bid_buy(self):
        pass

    def my_orders(self):
        pass

    def order_status(self):
        pass

    def remove_order(self):
        pass

    def ask_coin(self):
        pass

    def bid_coin(self):
        pass
