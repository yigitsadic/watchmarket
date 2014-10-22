# -*- coding: utf-8 -*-

import os


class AK47:
    def __init__(self):
        print u"BTCTURK Borsa Takip, Hoşgeldin Canım"        
        print u"Ne yapmak istersin?"        
        
    def _ask_what_to_do(self):
        print u"""
        Borsayı güncel şekilde takip  için: [1]
        Son 10 alım ve satım emirleri için: [2]
        """
        
        self.choice = raw_input(u"Secimin gunisigim?:\t")
        
        
    def _open_choice(self):
        if self.choice == '1':
            self._run_tracker()
        elif self.choice == '2':
            self._run_order_book()
        else:
            print u"İstediğin işlemi bulamadım güzelim."
        
    
    def _run_tracker(self):
        os.system('clear')
        from tracker import Tracker
        
        tracker = Tracker({'align': 'c', 'width': 20})
        tracker.run()
    
    def _run_order_book(self):
        os.system('clear')
        from order_book import OrderBook
        
        order_book = OrderBook()
        order_book.print_table()
        
        
    def shoot(self):
        self._ask_what_to_do()
        self._open_choice()
        
        
        
if __name__ == '__main__':
    weapon = AK47()
    weapon.shoot()