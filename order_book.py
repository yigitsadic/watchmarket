from btcturk_client.client import Btcturk
from texttable import Texttable

class OrderBook:
    """ Only lists top last ten buy and sell orders """
    
    def __init__(self):
        self.data_table = Texttable(max_width=400)
        self.data_table.set_cols_align(["c", "c", "c", "c"])

        self.data_table.add_row([
            'ALIS EMRI (TL)',
            'MIKTAR (BTC)',
            'SATIS EMRI (TL)',
            'MIKTAR (BTC)',
        ])
        
    
        self.btcturk = Btcturk()
        self.data_list =  self.btcturk.orderbook()


    def _table(self):
        buy_orders  = [element for element in self.data_list['Bids'][:10]]
        sell_orders = [element for element in self.data_list['Asks'][:10]]

        for i in range(0, 10):
            self.data_table.add_row([
                buy_orders[i][0],
                buy_orders[i][1],
                sell_orders[i][0],
                sell_orders[i][1]
            ])


        return self.data_table.draw()
        
        
    def print_table(self):
        print self._table()


if __name__ == '__main__':
    """ Run this shit baby! """
    
    order_book = OrderBook()    
    order_book.print_table()