from PriceGetter import PriceGetter
from Finder import Finder
pg = PriceGetter()
prices = pg.request()
for p in prices:
	print(p.toString())