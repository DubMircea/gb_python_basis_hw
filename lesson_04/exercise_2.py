from decimal import Decimal

import requests
import xml.etree.ElementTree as Et

BANK_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(currency_code):
    rates = {}

    request_response = requests.get(BANK_URL)

    if request_response.status_code == 200:
        root = Et.XML(request_response.content)
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

    res = rates.get(currency_code.upper(), {}).get('value')
    if res:
        res = Decimal(res.replace(',', '.'))

    return res


print(f"курс доллара {currency_rates('USD')}")
print(f"курс евро {currency_rates('eur')}")
