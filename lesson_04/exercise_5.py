import utils
import sys

if len(sys.argv) > 1:
    currency = sys.argv[1]
    val, dt = utils.currency_rates(currency)
    print(f'{val}, {dt}')
else:
    print(f'Sorry, not enough arguments')
