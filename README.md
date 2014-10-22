# BTCTURK Borsa Takip Betiği

![](https://en.bitcoin.it/w/images/en/5/50/Bitcoin.png)

**Neden?** Çünkü sayıları seviyorum.

## Gerekenler

* https://pypi.python.org/pypi/texttable
* https://github.com/emre/btcturk-client


##Kullanım

Kullanmak için
```python
# tracker
from tracker import Tracker

track_market = Tracker()

# or with options

track_market = Tracker({'width': 35, 'align': 'c'}, ['Ask', 'Bid', 'Timestamp'])

# and fly it

track_market.run()

```


## Son

Teşekkürler Emre client için. https://github.com/emre