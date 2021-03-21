import utils

val, dt = utils.currency_rates('USD')
print(f"курс доллара {val}, дата {dt}")

val, dt = utils.currency_rates('eur')
print(f"курс евро {val}, дата {dt}")
