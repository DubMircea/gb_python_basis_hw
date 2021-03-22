from decimal import Decimal

import requests
import xml.etree.ElementTree as Et
from datetime import datetime

BANK_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(currency_code):
    rates = {}
    date_str = ''

    request_response = requests.get(BANK_URL)

    if request_response.status_code == 200:
        root = Et.XML(request_response.content)
        date_str = root.attrib.get('Date')
        for element in root:
            num_code = element.find('NumCode').text
            char_code = element.find('CharCode').text
            nominal = element.find('Nominal').text
            name = element.find('Name').text
            value = element.find('Value').text
            rates[char_code] = {
                'num_code': num_code,
                'nominal': nominal,
                'name': name,
                'value': value,
            }

    res_value = rates.get(currency_code.upper(), {}).get('value')
    if res_value:
        res_value = Decimal(res_value.replace(',', '.'))

    if date_str:
        res_date = datetime.strptime(date_str, '%d.%m.%Y').date()
    else:
        res_date = None

    return res_value, res_date


val, dt = currency_rates('USD')
print(f"курс доллара {val}, дата {dt}")

val, dt = currency_rates('eur')
print(f"курс евро {val}, дата {dt}")
