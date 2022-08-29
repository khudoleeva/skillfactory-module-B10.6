
import requests
import json
from config import keys

class APIException(Exception):
	pass

class Converter:
	@staticmethod
	def get_price(quote, base, amount):
		try:
			quote_ticker = keys[quote]
		except KeyError:
			raise APIException('Некорректная валюта')
		try:
			base_ticker = keys[base]
		except KeyError:
			raise APIException('Некорректная валюта')
		try:
			d = float(amount)
		except ValueError:
			raise APIException('Некорректное количество валюты')
		if quote == base:
			raise APIException('Валюты не могут быть одинаковыми')
		r = requests.get(f"https://api.apilayer.com/fixer/convert?to={keys[base]}&from={keys[quote]}&amount={amount}", headers= {"apikey": "Rt2DJOAA5zlMR8zoq1ssmvToT9a63hZK"})
		h = f'Цена {amount} {quote}  ' + str(json.loads(r.content)['result'])+" " + f'в валюте {base}'
		return h





