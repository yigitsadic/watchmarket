# -*- coding: utf-8 -*-

import time
import datetime

from texttable import Texttable
from btcturk_client.client import Btcturk


class Tracker:
    def __init__(self, 
                options={
                    'width': 20,
                    'align': 'c',
                },
                columns=[
                    'Volume', 'Last', 'Timestamp',
                    'Bid', 'Ask', 'High', 'Low', 'Open']):

        """
            In 'options' option you can choose
            align and width for table output.
            
            In 'columns' option you can define
            which columns will be show.
            
            You can choose 8 columns:
                * Volume
                * Last
                * Timestamp
                * Bid
                * Ask
                * High
                * Low
                * Open
        """
        self.COLUMNS    = columns
        self.OPTIONS    = options        
        self.btcturk    = Btcturk()
        self.CHECK_TIME = self.OPTIONS.get('check', 60)

        self.HEADER_DICT = {
            'Volume': '24S HACIM (BTC)' ,
            'Last': 'SON ISLEM',
            'Timestamp': 'ZAMAN',
            'Bid': 'EN YUKSEK ALIS EMRI',
            'Ask': 'EN DUSUK SATIS EMRI',
            'High': 'EN YUKSEK',
            'Low': 'EN DUSUK',
            'Open': 'GUNUN ACILIS FIYATI'
        }


    
    def _create_table(self):
        self.data_table = Texttable(max_width=400)
        self.data_table.set_cols_align([self.OPTIONS['align'] for i in range(len(self.COLUMNS))])
        self.data_table.set_cols_width([self.OPTIONS['width'] for i in range(len(self.COLUMNS))])
        
        
    def _add_header(self):
        self.data_table.add_row([self.HEADER_DICT[column] for column in self.COLUMNS])
    
        
    def _wait(self):
        time.sleep(self.CHECK_TIME)
    
    
    def _print_values(self):
        values = self.btcturk.ticker()
    
        print self.data_table.draw()
        self.data_table._rows.pop()

        row = []
        
        for column in self.COLUMNS:
            if column == 'Timestamp':
                row.append(datetime.datetime.fromtimestamp(int(values['Timestamp'])).strftime('%H:%M:%S'))
            else:
                row.append(values[column])

        self.data_table.add_row(row)
        
    def run(self):
        self._create_table()
        self._add_header()
        
        while True:
            self._print_values()
            self._wait()


if __name__ == '__main__':
    options = {
        'align': 'c',
        'width': 20,
    }
    
    btctracker = Tracker(options=options, columns=['Ask', 'Bid', 'Timestamp'])
    btctracker.run()