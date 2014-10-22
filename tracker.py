# -*- coding: utf-8 -*-

import time
import datetime

from texttable import Texttable
from btcturk_client.client import Btcturk


class Tracker:
    def __init__(self):
        self.btcturk = Btcturk()
        self.CHECK_TIME = 60
        
    
    def _create_table(self):
        self.data_table = Texttable(max_width=400)
        self.data_table.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c"])
        self.data_table.set_cols_valign(["m", "m", "m", "m", "m", "m", "m", "m"])
        self.data_table.set_cols_width([17, 17, 17, 17, 17, 17, 17, 17])
        
        
    def _add_header(self):
        self.data_table.add_row([
            '24S HACIM (BTC)',
            'SON ISLEM',
            'ZAMAN',
            'EN YUKSEK ALIS EMRI',
            'EN DUSUK SATIS EMRI',
            'EN YUKSEK',
            'EN DUSUK',
            'GUNUN ACILIS FIYATI'
        ])


        
    def _wait(self):
        time.sleep(self.CHECK_TIME)
        
        
    def _get_values(self):
        values = self.btcturk.ticker()
    
        print self.data_table.draw()
        self.data_table._rows.pop()
    
        self.data_table.add_row([
            values['Volume'],
            values['Last'],
            datetime.datetime.fromtimestamp(int(values['Timestamp'])).strftime('%H:%M:%S'),
            values['Bid'],
            values['Ask'],        
            values['High'],
            values['Low'],
            values['Open']        
        ])
        
    def run(self):
        self._create_table()
        self._add_header()
        
        while True:
            self._get_values()
            self._wait()


if __name__ == '__main__':
    btctracker = Tracker()
    btctracker.run()
    