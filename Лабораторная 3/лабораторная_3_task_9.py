salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months):
    delta = spend - salary  # разница между зарплатой и расходами
    months -= 1  # уменьшение месяцев
    money_capital += delta  # суммирование разниц между зарплатой и расходами
    spend *= 1 + increase  # расчет увеличения рассходов
print(round(money_capital))
