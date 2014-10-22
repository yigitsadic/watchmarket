# BTCTURK Borsa Takip Betiği

![](https://en.bitcoin.it/w/images/en/5/50/Bitcoin.png)

**Neden?** Çünkü sayıları seviyorum.

## Gerekenler

* https://pypi.python.org/pypi/texttable
* https://github.com/emre/btcturk-client


##Kullanım

Kullanmak için farklı seçeneklere sahipsiniz.

```python
# tracker
from tracker import Tracker

track_market = Tracker()

# or with options

track_market = Tracker(options={
	'width': 35, 
	'align': 'c',
	'check': 20 # seconds
	},
	columns=['Ask', 'Bid', 'Timestamp']
)

# and run it

track_market.run()

# ...

#+----------------------+----------------------+----------------------+
#| EN DUSUK SATIS EMRI  | EN YUKSEK ALIS EMRI  |        ZAMAN         |
#+----------------------+----------------------+----------------------+
#+----------------------+----------------------+----------------------+
#|       884.460        |       875.560        |       22:00:44       |
#+----------------------+----------------------+----------------------+
#+----------------------+----------------------+----------------------+
#|       884.460        |       875.560        |       22:00:49       |
#+----------------------+----------------------+----------------------+

```


## Son

Teşekkürler Emre client için. https://github.com/emre