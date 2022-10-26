money_capital = 10000  # финансовая подушка безопасности
salary = 5000  # зарплата
spend = 6000   # расходы на проживание
increase = 0.05  # ежемесячный рост цен

month = 0  # количество месяцев, которое можно прожить

inflation = spend * increase
while money_capital + salary >= 0:
    if money_capital + salary > 0:
        money_capital -= spend
        money_capital -= inflation
        month += 1

print(month)
